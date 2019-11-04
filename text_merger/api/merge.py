import re
import difflib

clean_gold_re = re.compile("^\W*(.*\w)\W*$", re.U)

class Dictionary:
    def __init__(self, data):
        """
        The constructor.
        """
        self.gold = {}

        for line in data:
            fields = line.strip().split('\t')

            # hacks for handling non-standard orthography
            golds = set([fields[0],fields[0].replace(u"ſ",u"s"), clean_gold_re.sub("\\1",fields[0]), clean_gold_re.sub("\\1",fields[0].replace("ſ",u"s"))])
            for g in golds:
                if not g in self.gold:
                    self.gold[g] = 0
                if len(fields) > 1:
                    self.gold[g] += int(fields[1])
                else:
                    self.gold[g] += 1
    
    def lookup(self, string):
        """
        Look up a string in the dictionary and return its frequency.
        """
        return self.gold.get(string, -1)
    
    def competing_lookup(self, string1, string2):
        """
        Look up two strings in a dictionary and return the more frequent one.
        """
        if string1 in self.gold or string2 in self.gold:
            if self.lookup(string1) >= self.lookup(string2):
                return string1
            else:
                return string2
        else:
            cstring1 = clean_gold_re.sub("\\1",string1)
            cstring2 = clean_gold_re.sub("\\1",string2)
            if self.lookup(cstring1) >= self.lookup(cstring2):
                return string1
            else:
                return string2



class Merger:
    def __init__(self, gold):
        """
        The constructor.
        """
        self.gold = gold

    def merge(self, text, Text):
        """
        Merge two lines of text.
        """
        output = []

        # perform diff on line level
        diff = difflib.SequenceMatcher(None, text, Text)
        for tag, i1, i2, j1, j2 in diff.get_opcodes():
            if tag == "replace":
                left = text[i1:i2]
                right = Text[j1:j2]
                if len(left) != len(right):
                    #
                    # unequal size: fallback to character level
                    # searching for equal subsequences
                    lstream = " ".join(lword for lword in left)
                    rstream = " ".join(rword for rword in right)
                    diff2 = difflib.SequenceMatcher(None, lstream, rstream)
                    loutput = routput = ""
                    for tag2, I1, I2, J1, J2 in diff2.get_opcodes():
                        lseq = lstream[I1:I2]
                        rseq = rstream[J1:J2]
                        if tag2 == "replace" or tag2 == "equal":
                            min_len = min(len(lseq), len(rseq))
                            llonger = min_len == len(rseq)
                            for i in range(0,min_len):
                                if lseq[i] == " ":
                                    output.append(self.gold.competing_lookup(loutput, routput))
                                    loutput = routput = ""
                                    continue
                                loutput += lseq[i]
                                routput += rseq[i] 
                            if llonger:
                                for i in range(min_len,len(lseq)):
                                    if lseq[i] == " ":
                                        output.append(self.gold.competing_lookup(loutput, routput))
                                        loutput = routput = ""
                                        continue
                                    loutput += lseq[i]
                            else:
                                for i in range(min_len,len(rseq)):
                                    routput += rseq[i]
                        elif tag2 == "insert":
                            for i in range(0,len(rseq)):
                                if rseq[i] != " ":
                                    routput += rseq[i]
                        elif tag2 == "delete":
                            for i in range(0,len(lseq)):
                                if lseq[i] == " ":
                                    output.append(self.gold.competing_lookup(loutput, routput))
                                    loutput = routput = ""
                                    continue
                                loutput += lseq[i]
                    if loutput:
                        if self.gold.lookup(loutput) >= self.gold.lookup(routput):
                            output.append(loutput)
                        else:
                            output.append(routput)
                else:
                    for i in range(0,len(left)):
                        output.append(self.gold.competing_lookup(left[i], right[i]))

            elif tag == "insert":
                # TODO: something more clever?
                pass
            elif tag == "delete":
                # TODO: something more clever?
                for i in range(i1, i2):
                    output.append(text[i])
            else:
                for i in range(i1, i2):
                    output.append(text[i])


        return "".join(output)

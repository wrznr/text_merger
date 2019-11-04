
def lines(stream):
    # FIXME: Has probably to be replaced by a full-fledged tokenizer
    return [line.strip().split() for line in stream if line.strip()]

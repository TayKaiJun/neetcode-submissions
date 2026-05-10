class Solution:
    '''
    convert each char into its ascii and tokenize it with \
    e.g. "ABC" -> "\65\66\67\256"
    \256 is outside of the 256 extended ASCII set so it can be use as the separator
    '''
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            for l in word:
                asciiVal = ord(l)
                encoded += "\\" + str(asciiVal)
            encoded += "\\" + str(256)
        return encoded

    def decode(self, s: str) -> List[str]:
        asciiVals = s.split('\\')[1:]
        answer = []
        word = ""
        for asciiVal in asciiVals:
            asciiVal = int(asciiVal)
            if asciiVal == 256:
                answer.append(word)
                word = ""
            else:
                word += chr(asciiVal)
        return answer

class WordDictionary {
private:
struct TrieNode{
    bool isWord = false;
    TrieNode* letters[26]{};
    size_t minDepth = INT_MAX;
    size_t maxDepth = 0;
};

TrieNode* root = new TrieNode();
set<size_t> possibleLengths;

public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        TrieNode* curr = root;
        size_t len = word.length();
        possibleLengths.insert(len);

        for( int i = 0; i < len; i++ ){
            size_t index = word[i] - 'a';
            // update the min and max depth possible from this node
            curr->minDepth = min(len-i, curr->minDepth);
            curr->maxDepth = max(len-i, curr->maxDepth);
            if( !curr->letters[index] ){
                curr->letters[index] = new TrieNode();
            }
            curr = curr->letters[index];
        }
        curr->minDepth = 0;
        curr->maxDepth = max(curr->maxDepth, size_t{0});
        curr->isWord = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        size_t len = word.length();
        if(!possibleLengths.contains(len))
            return false;
        return dfs(word, 0, len, curr);
    }

    bool dfs( const string& word, size_t index, const size_t& len, TrieNode* curr ){
        // slight optimization - the rest of the word is not within a 
        // possible word length achieveable at the current node, prune the search
        if( len-index > curr->maxDepth || len-index < curr->minDepth)
            return false;

        for( int i = index; i < len; i++ ){
            if( word[i] == '.' ) {
                for( TrieNode* child : curr->letters ){
                    if( child && dfs(word, i+1, len, child) )
                        return true;
                }
                // if all the children returned False, we can return false now
                return false;
            }
            else{
                // if it's not wildcard, just progress normally
                size_t index = word[i] - 'a';
                curr = curr->letters[index];
                if( !curr ){
                    return false;
                }
            }
        }
        return curr->isWord;
        
    }
};

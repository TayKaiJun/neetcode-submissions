class WordDictionary {
private:
struct TrieNode{
    bool isWord = false;
    TrieNode* letters[26]{};
    // size_t minDepth;
    // size_t maxDepth;
};

TrieNode* root = new TrieNode();

public:
    WordDictionary() {
        
    }
    
    void addWord(string word) {
        TrieNode* curr = root;

        for( char c : word ){
            size_t len = word.length();
            size_t index = c - 'a';
            if( !curr->letters[index] ){
                curr->letters[index] = new TrieNode();
            }
            // curr->minDepth = min(len, curr->minDepth);
            // curr->maxDepth = max(len, curr->maxDepth);
            curr = curr->letters[index];
        }
        curr->isWord = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        size_t len = word.length();
        return dfs(word, 0, len, curr);
    }

    bool dfs( const string& word, size_t index, const size_t& len, TrieNode* curr ){
        for( int i = index; i < len; i++ ){
            if( word[i] == '.' ) {
                for( TrieNode* child : curr->letters ){
                    if( child && dfs(word, i+1, len, child) ) return true;
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

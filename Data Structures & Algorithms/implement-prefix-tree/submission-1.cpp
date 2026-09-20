struct PrefixNode{
    PrefixNode* letters[26]{};
    bool isWord = false;
};

class PrefixTree {
public:
    PrefixNode* root = new PrefixNode();

    PrefixTree() {
    }
    
    void insert(string word) {
        PrefixNode* curr = root;
        for( const char& l : word ){
            char t = l - 'a';
            if ( !curr->letters[t] ) {
                curr->letters[t] = new PrefixNode();
            }
            curr = curr->letters[t];
        }
        curr->isWord = true;
    }
    
    bool search(string word) {
        PrefixNode* curr = root;
        for( const char& l : word ){
            char t = l - 'a';
            curr = curr->letters[t];
            if( !curr ){
                return false;
            }
        }
        return curr->isWord;
    }
    
    bool startsWith(string prefix) {
        PrefixNode* curr = root;
        for( const char& l : prefix ){
            char t = l - 'a';
            curr = curr->letters[t];
            if( !curr ){
                return false;
            }
        }
        return true;
    }
};

struct PrefixNode{
    unordered_map< char, PrefixNode* > letters;
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
            if( !curr->letters.contains(l) ){
                curr->letters[l] = new PrefixNode();
            }
            curr = curr->letters[l];
        }
        curr->isWord = true;
    }
    
    bool search(string word) {
        PrefixNode* curr = root;
        for( const char& l : word ){
            if( !curr->letters.contains(l) ){
                return false;
            }
            curr = curr->letters[l];
        }
        return curr->isWord;
    }
    
    bool startsWith(string prefix) {
        PrefixNode* curr = root;
        for( const char& l : prefix ){
            if( !curr->letters.contains(l) ){
                return false;
            }
            curr = curr->letters[l];
        }
        return true;
    }
};

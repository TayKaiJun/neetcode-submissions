class Solution {

private:
    struct PrefixNode{
        PrefixNode* letters[26]{};
        const string* word = nullptr;
    };

    PrefixNode* root = new PrefixNode();

    void insert(const string& word) {
        PrefixNode* curr = root;
        for( const char& l : word ){
            char t = l - 'a';
            if ( !curr->letters[t] ) {
                curr->letters[t] = new PrefixNode();
            }
            curr = curr->letters[t];
        }
        curr->word = &word;
    }

    int boardRow;
    int boardCol;

public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        // form our prefixTree first
        for( const string& word: words ){
            insert(word);
        }

        vector<string> output;
        boardRow = board.size();
        boardCol = board[0].size();

        for( int i = 0; i < boardRow; i++ ){
            for( int j = 0; j < boardCol; j++){
                dfs(board, i, j, root, output );
            }
        }

        return output;
    }

    void dfs( vector<vector<char>>& board, int x, int y, PrefixNode* node, vector<string>& output ){
        if( x < 0 || x >= boardRow || y < 0 || y >= boardCol ){
            return;
        }
        if( board[x][y] == '.' ){
            return;
        }

        char l = board[x][y];
        PrefixNode* curr = node->letters[ l-'a' ];

        // our prefix node doesn't contain this letter. return
        if( !curr ){
            return;
        }

        // found a word, add to results
        if( curr->word ){
            output.push_back( *(curr->word) );
            curr->word = nullptr;
        }

        board[x][y] = '.';
        dfs(board, x+1, y, curr, output );
        dfs(board, x-1, y, curr, output );
        dfs(board, x, y+1, curr, output );
        dfs(board, x, y-1, curr, output );
        // backtrack, put l back into the original position
        board[x][y] = l;
        
    }
};
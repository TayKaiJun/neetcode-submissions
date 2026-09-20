class Solution {
private:
    size_t diff( string& word1, string& word2 ){
        size_t d = 0;
        for(int i = 0; i < word1.length(); i++ ){
            if( word1[i] != word2[i] )
                d++;
        }
        return d;
    }

    struct WordNode{
        set<WordNode*> neighbors;
        string word;
        bool visited = false;
    };

public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // if endWord not in wordList, impossible
        auto it = find(wordList.begin(), wordList.end(), endWord);
        if (it == wordList.end())
            return 0;

        // check if it's possible to start; if yes, track starting words
        vector<string> startingWords;
        for( auto word: wordList ){
            if( diff( beginWord, word ) == 1 ){
                startingWords.push_back( word );
            }
        }
        if( startingWords.empty() )
            return 0;

        // initialize bidirectional graph
        unordered_map<string, WordNode*> wordGraph;
        for( auto word: wordList ){
            wordGraph[word] = new WordNode();
            wordGraph[word]->word = word;
        }

        // setup graph connections
        for( int i = 0; i < wordList.size(); i++){
            for(int j = i+1; j < wordList.size(); j++ ){
                if( diff( wordList[i], wordList[j] ) == 1 ){
                    wordGraph[ wordList[i] ]->neighbors.insert( wordGraph[ wordList[j] ] );
                    wordGraph[ wordList[j] ]->neighbors.insert( wordGraph[ wordList[i] ] );
                }
            }
        }

        // for each starting point, do a bfs to find the shortest path.
        int steps = INT_MAX;
        bool possible = false;
        for( auto word: startingWords ){
            int sol = bfs( wordGraph, wordGraph[word], endWord );
            if( sol > 0 ){
                steps = min( steps, sol );
                possible = true;
            }
        }
        return possible ? steps : 0;
    }

    int bfs( unordered_map<string, WordNode*>& wordGraph, WordNode* node, string& target ) {
        cout << "In bfs\n";
        queue<tuple<WordNode*,size_t>> q;
        q.emplace(node,1);
        int steps = 0;
        WordNode* curr = nullptr;
        while( !q.empty() ){
            auto t = q.front();
            curr = get<0>(t);
            auto step = get<1>(t);
            cout << curr->word << '\n';
            curr->visited = true;
            q.pop();
            if( curr->word == target ){
                steps = step;
                break;
            }
            for( auto neighbor: curr->neighbors ){
                if( neighbor->visited == false )
                    q.emplace(neighbor, step+1);
            }
        }

        // clean up all the visited marker before the next bfs attempt
        for( auto it : wordGraph ){
            it.second->visited = false;
        }
        if( curr->word != target ){
            return 0;
        }
        return steps+1;
    }
};

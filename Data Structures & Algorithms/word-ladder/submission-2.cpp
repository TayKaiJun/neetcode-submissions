class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // if endWord not in wordList, impossible
        auto it = find(wordList.begin(), wordList.end(), endWord);
        if (it == wordList.end())
            return 0;
        
        // bfs - the first time hitting the target would be the shortest
        set<string> toVisit;
        for( auto word : wordList ){
            toVisit.insert(word);
        }

        queue<tuple<string,size_t>> q;
        q.emplace( beginWord, 1 );
        
        while( !q.empty() ){
            auto t = q.front();
            auto [ word, step ] = t;
            q.pop();
            
            if( word == endWord ){
                return step;
            }

            // go through all combinations of changing 1 letter in the word - O(26L)
            string temp = word;
            for( int i = 0; i < word.length(); i++ ){
                temp = word;
                for( int j = 0; j < 26; j++ ){
                    char l = 'a' + j;
                    temp[i] = l;
                    if( toVisit.contains(temp) ){
                        q.emplace(temp,step+1);
                        toVisit.erase(temp);
                    }
                }
            }
        }
        return 0;
    }
};

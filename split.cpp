char delimiter = ' ';

stringstream ss(text);
string word;
vector<string> words;
while(getline(ss, word, delimiter)) {
    words.push_back(word);
}

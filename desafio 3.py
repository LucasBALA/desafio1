# include <iostream>
# include <string>
# include <unordered_set>
using namespace std

// Expanda em ambas as direções de `low` e `high` para encontrar todos os palíndromos
void expand(string str, int low, int high, auto & set)
{
    // executa até que `str[low.high]` não seja um palíndromo
    while (low >= 0 & & high < str.length() & & str[low] == str[high])
    {
        // coloca todos os palíndromos em um conjunto
        set.insert(str.substr(low, high - low + 1))

        // Expandir em ambas as direções
        low--, high++
    }
}

// Função para encontrar todas as substrings palindrômicas únicas de uma determinada string
void findPalindromicSubstrings(string str)
{
    // cria um conjunto vazio para armazenar todas as substrings palindrômicas únicas
    unordered_set < string > set;

    for (int i=0; i < str.length(); i++)
    {
        // encontra todos os palíndromos de comprimento ímpar com `str[i]` como ponto médio
        expand(str, i, i, set);

        // encontra todos os palíndromos de comprimento par com `str[i]` e `str[i+1]` como
        // seus pontos médios
        expand(str, i, i + 1, set);}

    // imprime todas as substrings palindrômicas únicas
    for (auto i: set) {
        cout << i << " ";}
}

int main()
{
    string str = "google"

    findPalindromicSubstrings(str)

    return 0
}

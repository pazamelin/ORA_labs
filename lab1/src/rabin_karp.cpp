#include "str_match/rabin_karp.hpp"

#include <functional>
#include <algorithm>
#include <utility>

#define POLYNOMIAL_HASH_CONSTANT 33

namespace str_match
{
    std::pair<std::size_t, std::size_t>
    rabin_karp(const std::string& text, const std::string& pattern, std::size_t pos)
    {
        // hash pattern
        const std::size_t pattern_hash = detail::rolling_hash(pattern, 0, pattern.size());

        // hash a snippen of text of size equal to pattern's size 
        std::size_t subtext_hash = detail::rolling_hash(text, pos, pattern.size());

        // iterate over all such snippets
        for (; pos < text.size() - pattern.size() + 1; pos++)
        {
            // compare for match only if the hashs are equal
            if (subtext_hash == pattern_hash)
            {
                bool match = true;

                for (std::size_t i = 0; i < pattern.size(); i++)
                {
                    operations++;
                    if (text[pos + i] != pattern[i])
                    {
                        match = false;
                        break;
                    }
                }

                if (match)
                {
                    return {pos, operations}; // first match position in text 
                }
            }

            // update hash to the next snippet of the same size
            subtext_hash = detail::roll_hash(text, pos + 1, pattern.size(), subtext_hash);
        }

        return {text.size(), operations}; // match not found
    }

    namespace detail
    {        
        std::size_t pow(std::size_t base, std::size_t exp)
        {
            std::size_t result = 1;
            for (;;)
            {
                if (exp & 1)
                    result *= base;
                exp >>= 1;
                if (!exp)
                    break;
                base *= base;
            }

            return result;
        }

        std::size_t rolling_hash(const std::string& str, std::size_t pos, std::size_t len)
        {
            std::size_t result = 0;
            for (std::size_t i{0}; i < len; i++)
            {
                result += str[pos + i] * pow(POLYNOMIAL_HASH_CONSTANT, len - i - 1);
            }

            return result;
        }

        std::size_t roll_hash(const std::string& str, std::size_t pos, std::size_t len, std::size_t previous_hash)
        {
            previous_hash -= str[pos - 1] * pow(POLYNOMIAL_HASH_CONSTANT, len - 0 - 1);
            previous_hash *= POLYNOMIAL_HASH_CONSTANT;
            previous_hash += str[pos + len - 1];
            return previous_hash;
        }
        
    } // namespace detail

}  // namespace str_match

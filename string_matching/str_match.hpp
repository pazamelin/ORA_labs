#pragma once

#include <iterator>
#include <functional>
#include <utility>
#include <limits>

namespace str_match
{
    std::size_t naive(const std::string& text, const std::string& pattern, std::size_t pos)
    {
        for (; pos < text.size() - pattern.size() + 1; pos++)
        {
            bool match = true;

            for (std::size_t i = 0; i < pattern.size(); i++)
            {
                if (text[pos + i] != pattern[i])
                {
                    match = false;
                    break;
                }
            }

            if (match)
            {
                return pos;
            }

        }

        return text.size(); // match not found
    }

#define POLYNOMIAL_HASH_CONSTANT 33

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

    std::size_t advance(const std::string& str, std::size_t pos, std::size_t len, std::size_t previous)
    {
        previous -= str[pos - 1] * pow(POLYNOMIAL_HASH_CONSTANT, len - 0 - 1);
        previous *= POLYNOMIAL_HASH_CONSTANT;
        previous += str[pos + len - 1];
        return previous;
    }

    std::size_t rabin_karp(const std::string& text, const std::string& pattern, std::size_t pos)
    {
        const std::size_t pattern_hash = rolling_hash(pattern, 0, pattern.size());
        std::size_t subtext_hash = rolling_hash(text, pos, pattern.size());

        for (; pos < text.size() - pattern.size() + 1; pos++)
        {
            if (subtext_hash == pattern_hash)
            {
                bool match = std::equal(&pattern[0], &pattern[0] + pattern.size(), &text[pos]);
                if (match)
                {
                    return pos;
                }
            }

//            subtext_hash = rolling_hash(text, pos + 1, pattern.size());
          subtext_hash = advance(text, pos + 1, pattern.size(), subtext_hash);
        }

        return text.size(); // match not found
    }

}  // namespace str_match

#include "str_match/naive.hpp"

#include <functional>
#include <algorithm>
#include <utility>

namespace str_match
{
    std::pair<std::size_t, std::size_t>
    naive(const std::string& text, const std::string& pattern, std::size_t pos)
    {
        std::size_t operations = 0;

        // iterate over all snippets of text with the same size as pattern
        for (; pos < text.size() - pattern.size() + 1; pos++)
        {   // check every one of them for a match
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

        return {text.size(), operations}; // match not found
    }


}  // namespace str_match
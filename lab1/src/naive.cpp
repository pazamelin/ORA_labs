#include "str_match/naive.hpp"

#include <functional>
#include <algorithm>
#include <utility>

namespace str_match
{
    std::size_t naive(const std::string& text, const std::string& pattern, std::size_t pos)
    {
        // iterate over all snippets of text with the same size as pattern
        for (; pos < text.size() - pattern.size() + 1; pos++)
        {   // check every one of them for a match
            bool match = std::equal(&pattern[0], &pattern[0] + pattern.size(), &text[pos]);

            if (match)
            {
                return pos; // first match position in text 
            }

        }

        return text.size(); // match not found
    }


}  // namespace str_match
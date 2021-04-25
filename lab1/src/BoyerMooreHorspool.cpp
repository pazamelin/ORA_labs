#include "str_match/BoyerMooreHorspool.hpp"

#include <functional>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>

namespace str_match
{

	std::size_t boyer_moore_horspool(const std::string& text, const std::string& pattern, std::size_t pos) {
		int text_size = text.size();
		int pattern_size = pattern.size();
		if (pattern_size > text_size) {
			return text.size(); // match not found
		}
		if (pos != 0) {
			pos += pattern_size;
		}
		if (pos + pattern_size > text_size) {
			return text.size();
		}
		std::vector<int> offsetTable(256, pattern_size);
		for (size_t i = 0; i < pattern_size - 1; ++i) {
			offsetTable[(int)pattern[i]] = pattern_size - i - 1;
		}
		int i = pattern_size - 1;
		int j = i;
		int k = i;
		while ((j >= 0) && (i <= text_size - 1)) {
			j = pattern_size - 1;
			k = i;
			if (pos + k <= text_size) {
				while ((j >= 0) && (text[pos + k] == pattern[j])) {
					k--;
					j--;
				}
			}
			else {
				return text.size();
			}
			i += offsetTable[text[pos + i]];
		}
		if (j >= 0) {
			return text.size(); // match not found
		}
		else {
			return pos + k + 1;
		}
	}

}  // namespace str_match
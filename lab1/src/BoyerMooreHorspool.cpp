#include "str_match/BoyerMooreHorspool.hpp"

#include <functional>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>

namespace str_match
{

	std::pair<std::size_t, std::size_t> boyer_moore_horspool(const std::string& text, const std::string& pattern, std::size_t pos) {
		int text_size = text.size();
		int pattern_size = pattern.size();
		std::size_t counter = 0;
		bool flag = false;
		if (pattern_size > text_size) {
			std::pair<std::size_t, std::size_t> result = std::make_pair(text.size(), counter); 
			return result; // match not found
		}
		/*if (pos != 0) {
			pos += pattern_size;
		}*/
		if (pos + pattern_size > text_size) {
			std::pair<std::size_t, std::size_t> result = std::make_pair(text.size(), counter);
			return result; // match not found
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
				counter++;
				while ((j >= 0) && (text[pos + k] == pattern[j])) {
					k--;
					j--;
					counter++;
					flag = true;
				}
				if (flag) {
					counter--;
				}
				flag = false;
			}
			else {
				std::pair<std::size_t, std::size_t> result = std::make_pair(text.size(), counter);
				return result; // match not found
			}
			i += offsetTable[text[pos + i]];
		}
		if (j >= 0) {
			std::pair<std::size_t, std::size_t> result = std::make_pair(text.size(), counter);
			return result; // match not found
		}
		else {
			std::size_t ans = pos + k + 1;
			std::pair<std::size_t, std::size_t> result = std::make_pair(ans, counter);
			return result;
		}
	}

}  // namespace str_match
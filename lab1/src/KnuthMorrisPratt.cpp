#include "str_match/KnuthMorrisPratt.hpp"

#include <functional>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>

namespace str_match
{
	std::size_t  knuth_morris_pratt(const std::string& text, const std::string& pattern, std::size_t pos) {
		std::vector<std::size_t> pf(pattern.size());
		pf = detail::prefix_function(pattern);
		int k = 0;
		size_t index = text.size();
		for (size_t i = pos; i < text.size(); ++i) {
			while ((k > 0) && (pattern[k] != text[i])) {
				k = pf[k - 1];
			}
			if (pattern[k] == text[i]) {
				k++;
			}
			if (k == pattern.size()) {
				index = i - pattern.size() + 1;
				break;
			}
		}
		return index;
	}

	namespace detail
	{

		std::vector<std::size_t> prefix_function(const std::string& s) {
			size_t string_size = s.size();
			std::vector<std::size_t> prefix(string_size);
			for (size_t i = 1; i < string_size; ++i) {
				size_t j = prefix[i - 1];
				while ((j > 0) && (s[i] != s[j])) {
					j = prefix[j - 1];
				}
				if (s[i] == s[j]) {
					++j;
				}
				prefix[i] = j;
			}
			return prefix;
		}

	} // namespace detail

}  // namespace str_match
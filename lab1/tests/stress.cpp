#include "templates.hpp"

TEST_CASE("naive--rabin-karp", "[stress]")
{
    std::size_t text_size_min = 10;
    std::size_t text_size_max = 100;
    std::size_t text_size_step = 10;
    std::size_t iteration_per_size = 1000;
    std::size_t pattern_size = 2;

    stress_test(str_match::naive, str_match::rabin_karp,
                text_size_min,
                text_size_max,
                text_size_step,
                iteration_per_size,
                pattern_size
    );
}
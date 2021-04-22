#include "test_templates.hpp"

TEST_CASE("rabin-karp 1", "[unit]")
{
    const std::string text = "afuua";
    const std::string pattern = "fuu";

    std::size_t pos = str_match::rabin_karp(text, pattern, 0);
    REQUIRE(pos == 1);
}

TEST_CASE("rabin-karp 2", "[unit]")
{
    const std::string text = "sdfuusggfuux";
    const std::string pattern = "fuu";

    std::size_t pos = 0;
    pos = str_match::rabin_karp(text, pattern, pos);
    REQUIRE(pos == 2);

    pos = str_match::rabin_karp(text, pattern, pos + 3);
    REQUIRE(pos == 8);
}

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
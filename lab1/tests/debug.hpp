#define SEED RAND
#define PRINT_SEED 0
#define DEBUG_LOG

#include <random>

auto get_seed()
{
#if SEED == RAND
    std::random_device rd;
    const auto seed = rd();
#else
    const auto seed = SEED;
#endif

#if PRINT_SEED == 1
    std::cout << "SEED: " << seed << "\n";
#endif
    return seed;
}

template <typename Message, typename Value>
void debug_log(Message&& msg, Value&& value)
{
#ifdef DEBUG_LOG
    std::cerr << msg << " " << value << '\n';
#endif
}

template <typename Message>
void debug_log(Message&& msg)
{
#ifdef DEBUG_LOG
    std::cerr << msg << '\n';
#endif
}
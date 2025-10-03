unsigned total_amount_visible(unsigned top_num, unsigned num_of_sides) {
    unsigned sides_sum = (num_of_sides / 2) * (num_of_sides + 1);
    unsigned hidden_num = num_of_sides + 1 - top_num;
    return sides_sum - hidden_num;
}

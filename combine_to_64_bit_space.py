def combine_to_64_bit_space(left_hand, right_hand):
    combined_space = ''
    for left, right in zip(left_hand, right_hand):
        # Extract 5-bit values and combine
        combined_space += left[1] + right[1]
    
    # Truncate or pad to fit 64-bit space
    return combined_space[:64].ljust(64, '0')

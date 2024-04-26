def multi_stage_generator():
    """
    A generator function that yields at multiple points to demonstrate how
    execution state is maintained across yields.
    """
    print("Starting generator execution.")
    yield "First yield - initial stage"

    # Simulating some processing
    print("Processing between first and second yield")
    yield "Second yield - intermediate stage"

    # More processing
    print("Processing between second and third yield")
    yield "Third yield - final stage"

    print("Generator execution completed.")


def main():
    # Create the generator object
    gen = multi_stage_generator()

    # Iterate through the yields of the generator
    for value in gen:
        print(f"Received from generator: {value}")

    # Create the generator object
    gen = multi_stage_generator()

    # Manually fetch values from the generator using next()
    try:
        # First value
        first_stage = next(gen)
        print(f"Received from generator: {first_stage}")

        # Second value
        second_stage = next(gen)
        print(f"Received from generator: {second_stage}")

        # Third value
        third_stage = next(gen)
        print(f"Received from generator: {third_stage}")

        # Attempting to get a fourth value, which should raise StopIteration
        next(gen)
    except StopIteration:
        print("Generator has no more items to yield.")


if __name__ == "__main__":
    main()

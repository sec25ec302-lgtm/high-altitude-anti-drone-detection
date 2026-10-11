def get_environment(altitude):

    temperature = 15 - (0.0065 * altitude)

    pressure = 1013.25 * (
        1 - 2.25577e-5 * altitude
    ) ** 5.25588

    return temperature, pressure

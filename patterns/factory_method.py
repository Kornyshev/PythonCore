class Transport:
    """ Abstract transport class """

    def deliver(self):
        pass


class Truck(Transport):
    """ Concrete implementation of a truck transport """

    def deliver(self):
        return "Delivering by land in a box."


class Ship(Transport):
    """ Concrete implementation of a ship transport """

    def deliver(self):
        return "Delivering by sea in a container."


class Airplane(Transport):
    """ Concrete implementation of an airplane transport """

    def deliver(self):
        return "Delivering by air in a cargo hold."


class TransportFactory:
    """ Factory class to create different types of transport """

    @staticmethod
    def get_transport(transport_type):
        if transport_type == 'truck':
            return Truck()
        elif transport_type == 'ship':
            return Ship()
        elif transport_type == 'airplane':
            return Airplane()
        raise ValueError('Unknown transport type')


def main():
    transport_type = input("Enter the type of transport (truck, ship, airplane): ")
    try:
        transport = TransportFactory.get_transport(transport_type.lower())
        print(transport.deliver())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

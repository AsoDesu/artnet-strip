import stupidArtnet

class ArtNetReceiver:
    def __init__(self, data_method, universe: int = 0):
        self.node = stupidArtnet.StupidArtnetServer()
        self.data_method = data_method

        # universes are 0 indexed
        self.node.register_listener(universe=(universe - 1), callback_function=data_method)

    def disconnect(self):
        self.node.close()
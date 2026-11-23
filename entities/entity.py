class Entity:
    def __init__ (
        self,
        nome : str = '',
        idade : str = '',
        carnivoro : bool = False,
        especie : str = '',
        id : str | None : None,
    ) -> None:
        super().__init__(id=id)
        self.nome = nome,
        self.idade = idade,
        self.carnivoro,
        self.especie = especie
        
        def __repr__(self) -> str:
        return (
            f"Dinosssauro(id={self.id}, nome={self.nome!r}"
            f"idade={self.idade!r}, carnivoro={self.carnivoro!r}, especie={self.especie}"
        )
        
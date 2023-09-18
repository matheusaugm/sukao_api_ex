-- Cria uma tabela
CREATE TABLE
    IF NOT EXISTS produto (
        id SERIAL PRIMARY KEY,
        codigo INTEGER NOT NULL,
        produto VARCHAR(255) NOT NULL,
        valor FLOAT NOT NULL,
        ingredientes VARCHAR(255)
    );
-- Insere dados na tabela
INSERT INTO
    produto (
        codigo,
        produto,
        valor,
        ingredientes
    )
VALUES (
        1,
        'Atum',
        24.00,
        '(atum, cenoura, ricota, azeitona, cebola, alface e tomate)'
    ), (
        2,
        'Frango',
        24.00,
        '(frango desfiado, milho, catupiry, batata palha, molho especial, alface e tomate)'
    ), (
        3,
        'Peito de Peru',
        24.00,
        '(peito de peru, queijo minas, abacaxi, molho especial, alface e tomate)'
    ), (
        4,
        'Presunto',
        20.00,
        '(presunto, muçarela, molho especial, alface e tomate)'
    ), (
        5,
        'Salpicão',
        24.00,
        '(frango desfiado, maionese, milho, azeitona, cenoura, passas, batata palha, alface e tomate)'
    ), (
        6,
        'Maxburguer',
        24.00,
        '(hamburguer bovino artesanal, muçarela, molho especial, alface e tomate)'
    ), (
        7,
        'Havaiano',
        28.00,
        '(hamburguer bovino artesanal, muçarela, molho especial, alface e tomate)'
    ), (
        8,
        'Framburguer',
        32.00,
        '(hamburguer de frango artesanal,muçarela bacon,molho especial alface e tomate)'
    ), (
        9,
        'Sukão',
        32.00,
        '(hamburguer bovino artesanal,muçarela,presunto,batata palha ovo bacon,molho especial alface e tomate)'
    );
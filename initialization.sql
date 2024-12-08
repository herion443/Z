-- Створення таблиці постачальників
CREATE TABLE Suppliers (
    supplier_id BIGSERIAL PRIMARY KEY,
    supplier_name VARCHAR(255) NOT NULL,
    contact_info TEXT
);

-- Створення таблиці книг
CREATE TABLE Books (
    book_id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    genre VARCHAR(100),
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

-- Створення таблиці продажів
CREATE TABLE Sales (
    sale_id BIGSERIAL PRIMARY KEY,
    sale_date DATE NOT NULL,
    customer_name VARCHAR(255),
    total_amount DECIMAL(10, 2) NOT NULL
);

-- Створення таблиці деталей продажів
CREATE TABLE SaleDetails (
    sale_detail_id BIGSERIAL PRIMARY KEY,
    sale_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES Sales(sale_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Додавання початкових даних до таблиці постачальників
INSERT INTO Suppliers (supplier_name, contact_info) VALUES
('ТОВ Книжкова планета', 'тел: +380123456789, email: bookplanet@example.com'),
('Видавництво Ранок', 'тел: +380987654321, email: ranok@example.com');

-- Додавання початкових даних до таблиці книг
INSERT INTO Books (title, author, genre, price, stock_quantity, supplier_id) VALUES
('Гаррі Поттер і філософський камінь', 'Дж. К. Ролінг', 'Фентезі', 350.00, 20, 1),
('Мистецтво війни', 'Сунь-Цзи', 'Філософія', 250.00, 15, 2),
('Три товариші', 'Еріх Марія Ремарк', 'Роман', 300.00, 10, 1);

-- Додавання початкових даних до таблиці продажів
INSERT INTO Sales (sale_date, customer_name, total_amount) VALUES
('2024-12-01', 'Олена Петрова', 750.00),
('2024-12-02', 'Іван Іванов', 600.00);

-- Додавання початкових даних до таблиці деталей продажів
INSERT INTO SaleDetails (sale_id, book_id, quantity, subtotal) VALUES
(1, 1, 2, 700.00),
(1, 3, 1, 300.00),
(2, 2, 2, 500.00),
(2, 3, 1, 300.00);
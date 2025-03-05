-- Таблица пользователей
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, 
    username VARCHAR(50) NOT NULL UNIQUE, 
    password_hash VARCHAR(255) NOT NULL, 
    email VARCHAR(100) NOT NULL UNIQUE, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- Таблица счетов
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY, 
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, 
    account_name VARCHAR(100) NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    currency VARCHAR(10) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Таблица категорий
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY, 
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, 
    category_name VARCHAR(100) NOT NULL, 
    category_type VARCHAR(10) CHECK (category_type IN ('income', 'expense')), 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- Таблица транзакций
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, 
    account_id INT REFERENCES accounts(account_id) ON DELETE CASCADE, 
    category_id INT REFERENCES categories(category_id) ON DELETE SET NULL, 
    amount DECIMAL(15, 2) NOT NULL, 
    transaction_type VARCHAR(10) CHECK (transaction_type IN ('income', 'expense')), 
    description TEXT, 
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- Таблица бюджетов
CREATE TABLE budgets (
    budget_id SERIAL PRIMARY KEY, 
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, 
    category_id INT REFERENCES categories(category_id) ON DELETE CASCADE,
    amount DECIMAL(15, 2) NOT NULL, 
    start_date DATE NOT NULL, 
    end_date DATE NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

-- Таблица целей
CREATE TABLE goals (
    goal_id SERIAL PRIMARY KEY, 
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, 
    goal_name VARCHAR(100) NOT NULL, 
    target_amount DECIMAL(15, 2) NOT NULL, 
    current_amount DECIMAL(15, 2) DEFAULT 0.00, 
    deadline DATE, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

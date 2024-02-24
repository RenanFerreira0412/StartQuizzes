CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    title VARCHAR (100) NOT NULL,
    type VARCHAR (50) NOT NULL,
    category VARCHAR (50) NOT NULL,
    fk_users_id INTEGER
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR (50),
    email VARCHAR (50) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    prompt VARCHAR (255) NOT NULL,
    answer CHAR NOT NULL,
    fk_quizzes_id INTEGER
);

CREATE TABLE options (
    id SERIAL PRIMARY KEY,
    a VARCHAR (255) NOT NULL,
    b VARCHAR (255) NOT NULL,
    c VARCHAR (255) NOT NULL,
    d VARCHAR (255) NOT NULL,
    fk_questions_id INTEGER
);

CREATE TABLE ranks (
    id SERIAL PRIMARY KEY,
    time INTEGER NOT NULL,
    fk_quizzes_id INTEGER,
    fk_users_id INTEGER
);
 
ALTER TABLE quizzes ADD CONSTRAINT FK_quizzes_2
    FOREIGN KEY (fk_users_id)
    REFERENCES users (id)
    ON DELETE CASCADE;
 
ALTER TABLE questions ADD CONSTRAINT FK_questions_2
    FOREIGN KEY (fk_quizzes_id)
    REFERENCES quizzes (id)
    ON DELETE RESTRICT;
 
ALTER TABLE options ADD CONSTRAINT FK_options_2
    FOREIGN KEY (fk_questions_id)
    REFERENCES questions (id)
    ON DELETE RESTRICT;
 
ALTER TABLE ranks ADD CONSTRAINT FK_ranks_2
    FOREIGN KEY (fk_quizzes_id)
    REFERENCES quizzes (id)
    ON DELETE CASCADE;
 
ALTER TABLE ranks ADD CONSTRAINT FK_ranks_3
    FOREIGN KEY (fk_users_id)
    REFERENCES users (id)
    ON DELETE CASCADE;
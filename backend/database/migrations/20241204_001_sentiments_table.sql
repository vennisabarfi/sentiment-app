CREATE TABLE sentiments (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_comment_id INT NOT NULL REFERENCES user_comments(id) ON DELETE CASCADE,
    sentiment_rating DECIMAL(3, 2) NOT NULL, -- e.g., range 0.0 to 1.0
    sentiment_label TEXT NOT NULL,          -- e.g., 'positive', 'neutral', 'negative'
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

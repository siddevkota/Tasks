CREATE TABLE IF NOT EXISTS versions (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100),
    version VARCHAR(50),
    deployed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO versions (model_name, version) VALUES
('baseline_model', 'v1.0');

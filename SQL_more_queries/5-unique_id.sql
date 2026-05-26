-- Create the table unique_id if it doesn't exist.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY (id),
    UNIQUE (id)
);

-- Set the default value for the id column to 1.
ALTER TABLE unique_id
MODIFY COLUMN id INT NOT NULL DEFAULT 1;

EXIT

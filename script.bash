# Tạo database tên phamdoancanh
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS phamdoancanh;"

# Khởi tạo table để lưu dataset
mysql -u root -p -e "
USE phamdoancanh;
CREATE TABLE restaurant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    keysData VARCHAR(255),
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    name VARCHAR(255),
    postalcode VARCHAR(200),
    websites VARCHAR(2083),
    province VARCHAR(100)
);"


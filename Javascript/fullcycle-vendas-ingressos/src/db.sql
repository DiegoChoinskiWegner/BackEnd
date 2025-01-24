use tickets;

CREATE TABLE if NOT EXISTS 'mydb'.'users' (
    'id'
    'company_name'
    'cerated_at'
    'updated_at'
    'user_id'
    PRIMARY KEY ('id'),
    INDEX 'fk_partners_users1_idx' ('user_id' ASC) VISIBLE,
    CONSTRAINT 'fk_partners_users1'
    FOREIGN KEY ('user_id')
    REFERENCES 'mydb'.'users' ('id')
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE if NOT EXISTS 'mydb'.'partners' (
    'id'
    'company_name'
    'cerated_at'
    'updated_at'
    'user_id'
    PRIMARY KEY ('id'),
    INDEX 'fk_partners_users1_idx' ('user_id' ASC) VISIBLE,
    CONSTRAINT 'fk_partners_users1'
    FOREIGN KEY ('user_id')
    REFERENCES 'mydb'.'users' ('id')
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE if NOT EXISTS 'mydb'.'customers' (
    'id'
    'company_name'
    'cerated_at'
    'updated_at'
    'user_id'
    PRIMARY KEY ('id'),
    INDEX 'fk_partners_users1_idx' ('user_id' ASC) VISIBLE,
    CONSTRAINT 'fk_partners_users1'
    FOREIGN KEY ('user_id')
    REFERENCES 'mydb'.'users' ('id')
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE if NOT EXISTS 'mydb'.'events' (
    'id'
    'company_name'
    'cerated_at'
    'updated_at'
    'user_id'
    PRIMARY KEY ('id'),
    INDEX 'fk_partners_users1_idx' ('user_id' ASC) VISIBLE,
    CONSTRAINT 'fk_partners_users1'
    FOREIGN KEY ('user_id')
    REFERENCES 'mydb'.'users' ('id')
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE if NOT EXISTS 'mydb'.'tickets' (
    'id'
    'company_name'
    'cerated_at'
    'updated_at'
    'user_id'
    PRIMARY KEY ('id'),
    INDEX 'fk_partners_users1_idx' ('user_id' ASC) VISIBLE,
    CONSTRAINT 'fk_partners_users1'
    FOREIGN KEY ('user_id')
    REFERENCES 'mydb'.'users' ('id')
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;




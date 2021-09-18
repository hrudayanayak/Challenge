# This is the Random password generator to not password in clear text
resource "random_password" "password" { 
  length           = 16
  special          = true
  override_special = "_%@/'\""
}

# DB resource paramters DB engine instance size credentilas
resource "aws_db_instance" "db" {
  allocated_storage      = 10
  engine                 = "mysql"
  engine_version         = "8.0"
  instance_class         = "db.t2.micro"
  identifier             = "${var.namespace}-db-instance"
  name                   = "dev-db"
  username               = "admin"
  password               = random_password.password.result
  db_subnet_group_name   = var.vpc.db_subnet_group 
  vpc_security_group_ids = [var.sg.db] 
  skip_final_snapshot    = true
}

output "DATABASE_NAME" {
  value = module.dynamo.dynamodb_table_id
}
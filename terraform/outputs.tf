output "instance_public_ip" {
  description = "The public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}

output "instance_url" {
  description = "The URL of the application"
  value       = "http://${aws_instance.app_server.public_ip}:${var.app_port}"
}

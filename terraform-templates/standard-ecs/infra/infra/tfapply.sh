#!/bin/bash

echo "[Info]::[compiling Terraform configuration]"
python platform-builder.py

echo "[Info]::[Running Terraform Plan]::[passive reality check]"
terraform plan -parallelism=10

echo "[Info]::[Last chance to Quit]::[Waiting 10s to apply above updates]"
sleep 10

echo "[Info]::[Applying above Terraform updates]"
terraform apply -parallelism=10
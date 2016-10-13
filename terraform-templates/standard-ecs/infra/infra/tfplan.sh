#!/bin/bash

echo "[Info]::[compiling Terraform configuration]"
python platform-builder.py

echo "[Info]::[Running Terraform Plan]::[passive reality check]"
terraform plan -parallelism=10

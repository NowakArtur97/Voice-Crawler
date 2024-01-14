# Voice-Crawler

## Table of Contents

- [General info](#general-info)
- [Features](#features)
- [Built With](#built-with)
- [Status](#status)

## General info

AWS CloudFormation template with resources to automatically create transcriptions of mp3 files added to the S3 bucket using Amazon Trascribe.

## Features

- Triggering the lambda function after adding an mp3 file to the S3 bucket
- Creating a transcription from an audio file added to an S3 bucket and saving the response in json format in another bucket
- Automatic cleaning of S3 buckets after deleting a Cloudformation template
- Collecting logs from the lambda function responsible for transcribing audio files

## Built With

Cloudformation resources:

- S3 Buckets
- IAM Roles
- IAM Policy
- Lambda Permission
- Lambda Functions
- CloudFormation Custom Resource
- Log Group

## Status

Project is: finished

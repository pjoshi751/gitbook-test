# Architecture Principles 
[Architecture Principles](MOSIP-Architecture-Principles.md)

# Modules 
* [Pre-Registration](Pre-Registration.md) 
* Registration
* Registration Processor
* ID Authentication
* Resident Services
* Partner Management
* Admin

# Test Table
col1|col2|col3
---|---|---
r11|r12|r13
r21|r22|r23

# Functional Architecture
![](_images/MOSIP_functional_architecture.png) 

# Logical Architecture
![](_images/arch_diagrams/MOSIP_logical_architecture_v0.1.png) 

# Data Architecture
[MOSIP Data Architecture](MOSIP-Data-Architecture.md) 

# Design choices
* Microservice based architecture for all platform services for modularity and scalability.
* Staged Event Driven Architecture (SEDA) for processing Registration data for extensibility.
* Thick client architecture for Registration client

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

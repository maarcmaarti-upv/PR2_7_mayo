--Este código crea las tablas para la BD, esta es la parte de la entrega que forma parte de la asignatura de GDI

--Nuevo esquema

CREATE SCHEMA IF NOT EXISTS pimientos;
SET search_path TO pimientos;

-- Proveedor

CREATE TABLE IF NOT EXISTS proveedor (
    nombre      VARCHAR(150) PRIMARY KEY,
    direccion   VARCHAR(250) NOT NULL,
    telefono    INTEGER NOT NULL
);

-- Albaran_Proveedor

CREATE TABLE IF NOT EXISTS albaran_proveedor (
    nombre      VARCHAR(150) NOT NULL,
    albaran     VARCHAR(50) NOT NULL,

    CONSTRAINT pk_albaran_proveedor
        PRIMARY KEY (nombre, albaran),

    CONSTRAINT fk_albaran_proveedor_nombre
        FOREIGN KEY (nombre)
        REFERENCES proveedor(nombre)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
=
-- Cliente

CREATE TABLE IF NOT EXISTS cliente (
    nombre      VARCHAR(150) PRIMARY KEY,
    direccion   VARCHAR(250) NOT NULL,
    telefono    INTEGER NOT NULL
);

-- Albaran_Cliente

CREATE TABLE IF NOT EXISTS albaran_cliente (
    nombre      VARCHAR(150) NOT NULL,
    albaran     VARCHAR(50) NOT NULL,

    CONSTRAINT pk_albaran_cliente
        PRIMARY KEY (nombre, albaran),

    CONSTRAINT fk_albaran_cliente_nombre
        FOREIGN KEY (nombre)
        REFERENCES cliente(nombre)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Pallet

CREATE TABLE IF NOT EXISTS pallet (
    codigo      VARCHAR(50) PRIMARY KEY,
    tamano      NUMERIC(10,2) NOT NULL,
    material    VARCHAR(100) NOT NULL
);

-- Caja

CREATE TABLE IF NOT EXISTS caja (
    codigo          VARCHAR(50) PRIMARY KEY,
    tamano          NUMERIC(10,2) NOT NULL,
    material        VARCHAR(100) NOT NULL,
    codigo_pallet   VARCHAR(50) NOT NULL,

    CONSTRAINT fk_caja_pallet
        FOREIGN KEY (codigo_pallet)
        REFERENCES pallet(codigo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Paquete

CREATE TABLE IF NOT EXISTS paquete (
    codigo        VARCHAR(50) PRIMARY KEY,
    tamano        NUMERIC(10,2) NOT NULL,
    material      VARCHAR(100) NOT NULL,
    codigo_caja   VARCHAR(50) NOT NULL,

    CONSTRAINT fk_paquete_caja
        FOREIGN KEY (codigo_caja)
        REFERENCES caja(codigo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Lote_Pimientos

CREATE TABLE IF NOT EXISTS lote_pimientos (
    numero           VARCHAR(50) PRIMARY KEY,
    color            VARCHAR(50) NOT NULL,
    peso             NUMERIC(10,2) NOT NULL,
    procedencia      VARCHAR(150) NOT NULL,
    precio           NUMERIC(10,2) NOT NULL,
    codigo_paquete   VARCHAR(50) NOT NULL,

    CONSTRAINT fk_lote_paquete
        FOREIGN KEY (codigo_paquete)
        REFERENCES paquete(codigo)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Venden

CREATE TABLE IF NOT EXISTS venden (
    proveedor    VARCHAR(150) NOT NULL,
    lote         VARCHAR(50) NOT NULL,
    transporte   VARCHAR(100) NOT NULL,
    km           NUMERIC(10,2) NOT NULL,
    duracion     NUMERIC(10,2) NOT NULL,

    CONSTRAINT pk_venden
        PRIMARY KEY (proveedor, lote),

    CONSTRAINT fk_venden_proveedor
        FOREIGN KEY (proveedor)
        REFERENCES proveedor(nombre)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_venden_lote
        FOREIGN KEY (lote)
        REFERENCES lote_pimientos(numero)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Comprado

CREATE TABLE IF NOT EXISTS comprado (
    cliente      VARCHAR(150) NOT NULL,
    pallet       VARCHAR(50) NOT NULL,
    transporte   VARCHAR(100) NOT NULL,
    km           NUMERIC(10,2) NOT NULL,
    duracion     NUMERIC(10,2) NOT NULL,

    CONSTRAINT pk_comprado
        PRIMARY KEY (cliente, pallet),

    CONSTRAINT fk_comprado_cliente
        FOREIGN KEY (cliente)
        REFERENCES cliente(nombre)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_comprado_pallet
        FOREIGN KEY (pallet)
        REFERENCES pallet(codigo)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

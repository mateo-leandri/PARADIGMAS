PGDMP     6        	            {            tp1_p3_paradigmas_db    15.3    15.3                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16431    tp1_p3_paradigmas_db    DATABASE     �   CREATE DATABASE tp1_p3_paradigmas_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Spain.1252';
 $   DROP DATABASE tp1_p3_paradigmas_db;
                postgres    false                       0    0    DATABASE tp1_p3_paradigmas_db    ACL     5   GRANT ALL ON DATABASE tp1_p3_paradigmas_db TO mateo;
                   postgres    false    3334            �            1259    16440    cuotas    TABLE     �   CREATE TABLE public.cuotas (
    id smallint NOT NULL,
    id_lote smallint,
    valor integer,
    estado character varying(15),
    venc date
);
    DROP TABLE public.cuotas;
       public         heap    postgres    false            �            1259    16437    factor_ubicaciones    TABLE     e   CREATE TABLE public.factor_ubicaciones (
    ubicacion character varying(15),
    factor smallint
);
 &   DROP TABLE public.factor_ubicaciones;
       public         heap    postgres    false            �            1259    16432    lotes    TABLE       CREATE TABLE public.lotes (
    id smallint NOT NULL,
    estado character varying(15),
    medida_m2 smallint,
    ubicacion character varying(15),
    descripcion character varying(300),
    precio_total integer,
    precio_anticipo integer,
    duenio_dni smallint
);
    DROP TABLE public.lotes;
       public         heap    postgres    false                       0    16440    cuotas 
   TABLE DATA           B   COPY public.cuotas (id, id_lote, valor, estado, venc) FROM stdin;
    public          postgres    false    216          �          0    16437    factor_ubicaciones 
   TABLE DATA           ?   COPY public.factor_ubicaciones (ubicacion, factor) FROM stdin;
    public          postgres    false    215   0       �          0    16432    lotes 
   TABLE DATA           y   COPY public.lotes (id, estado, medida_m2, ubicacion, descripcion, precio_total, precio_anticipo, duenio_dni) FROM stdin;
    public          postgres    false    214   �       o           2606    16444    cuotas cuotas_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.cuotas
    ADD CONSTRAINT cuotas_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.cuotas DROP CONSTRAINT cuotas_pkey;
       public            postgres    false    216            m           2606    16436    lotes lotes_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.lotes
    ADD CONSTRAINT lotes_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.lotes DROP CONSTRAINT lotes_pkey;
       public            postgres    false    214                   x������ � �      �   @   x�H-��M-)J��4�40���+I-�MM���4215�rN��IU(��K�, *2� *����� &f	      �   �   x�m���0Eg�+�Q[(�cCYxL]LbA�࠴��I�,KG~���v�-�;y�e��Fz�W�.��cd	8��!��	�Qc�я[ˉ�σ���D3��ԥ��ݡ�;Φ'Cb.4=��4��"K5ڭ*>���w�:�V?���j���9�[��z.iH     
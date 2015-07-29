--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.9
-- Dumped by pg_dump version 9.4.0
-- Started on 2015-07-19 16:17:22 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- TOC entry 2081 (class 0 OID 17459)
-- Dependencies: 190
-- Data for Name: mufi_site; Type: TABLE DATA; Schema: public; Owner: myprojectdbuser
--

INSERT INTO mufi_site (id, name, url, date_created, trash) VALUES (1, 'Ютуб', 'www.youtube.com', '2015-07-18 16:25:52+03', false);
INSERT INTO mufi_site (id, name, url, date_created, trash) VALUES (3, 'Ютуб краткий (с временной меткой)', 'youtu.be', '2015-07-18 18:21:50+03', false);
INSERT INTO mufi_site (id, name, url, date_created, trash) VALUES (4, 'youtube.com', 'youtube.com', '2015-07-18 18:47:21+03', false);


--
-- TOC entry 2090 (class 0 OID 0)
-- Dependencies: 189
-- Name: mufi_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myprojectdbuser
--

SELECT pg_catalog.setval('mufi_site_id_seq', 4, true);


--
-- TOC entry 2083 (class 0 OID 17514)
-- Dependencies: 194
-- Data for Name: mufi_state; Type: TABLE DATA; Schema: public; Owner: myprojectdbuser
--

INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (1, 'video_loading', '2015-07-18 17:51:10+03', false, 'выполняется загрузка видео');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (2, 'video_loading_success', '2015-07-18 17:51:22+03', false, 'загрузка видео выполнена успешно');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (3, 'video_loading_error', '2015-07-18 17:51:32+03', false, 'загрузка видео выполнена с ОШИБКОЙ');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (4, 'sound_process', '2015-07-18 17:51:37+03', false, 'выполняется обработка звука');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (5, 'sound_process_success', '2015-07-18 17:51:43+03', false, 'обработка звука выполнена успешно');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (6, 'sound_process_error', '2015-07-18 17:51:49+03', false, 'обработка звука выполнена с ОШИБКОЙ');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (7, 'sound_search', '2015-07-18 17:51:55+03', false, 'выполняется поиск названия аудио-трека');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (8, 'sound_search_success', '2015-07-18 17:52:01+03', false, ' поиск названия аудио-трека выполнен успешно');
INSERT INTO mufi_state (id, name, date_created, trash, description) VALUES (9, 'sound_search_error', '2015-07-18 17:52:06+03', false, 'поиск названия аудио-трека выполнен с ОШИБКОЙ');


--
-- TOC entry 2091 (class 0 OID 0)
-- Dependencies: 193
-- Name: mufi_state_id_seq; Type: SEQUENCE SET; Schema: public; Owner: myprojectdbuser
--

SELECT pg_catalog.setval('mufi_state_id_seq', 9, true);


-- Completed on 2015-07-19 16:17:22 MSK

--
-- PostgreSQL database dump complete
--


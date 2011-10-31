--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO ltmo;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO ltmo;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO ltmo;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO ltmo;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_message; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE auth_message (
    id integer NOT NULL,
    user_id integer NOT NULL,
    message text NOT NULL
);


ALTER TABLE public.auth_message OWNER TO ltmo;

--
-- Name: auth_message_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE auth_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_message_id_seq OWNER TO ltmo;

--
-- Name: auth_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE auth_message_id_seq OWNED BY auth_message.id;


--
-- Name: auth_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('auth_message_id_seq', 12, true);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO ltmo;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO ltmo;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('auth_permission_id_seq', 36, true);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    password character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO ltmo;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO ltmo;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO ltmo;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO ltmo;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('auth_user_id_seq', 3, true);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO ltmo;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO ltmo;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO ltmo;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO ltmo;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 12, true);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO ltmo;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO ltmo;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('django_content_type_id_seq', 12, true);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO ltmo;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO ltmo;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO ltmo;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Name: ltmo_leak; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE ltmo_leak (
    id integer NOT NULL,
    slug character varying(50),
    title character varying(126),
    description text NOT NULL,
    author character varying(20) NOT NULL,
    created timestamp with time zone NOT NULL,
    changed timestamp with time zone NOT NULL,
    tags character varying(255) NOT NULL,
    metadata text NOT NULL,
    rendered text
);


ALTER TABLE public.ltmo_leak OWNER TO ltmo;

--
-- Name: ltmo_leak_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE ltmo_leak_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.ltmo_leak_id_seq OWNER TO ltmo;

--
-- Name: ltmo_leak_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE ltmo_leak_id_seq OWNED BY ltmo_leak.id;


--
-- Name: ltmo_leak_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('ltmo_leak_id_seq', 92, true);


--
-- Name: south_migrationhistory; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE south_migrationhistory (
    id integer NOT NULL,
    app_name character varying(255) NOT NULL,
    migration character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.south_migrationhistory OWNER TO ltmo;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE south_migrationhistory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.south_migrationhistory_id_seq OWNER TO ltmo;

--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE south_migrationhistory_id_seq OWNED BY south_migrationhistory.id;


--
-- Name: south_migrationhistory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('south_migrationhistory_id_seq', 2, true);


--
-- Name: tagging_tag; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE tagging_tag (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.tagging_tag OWNER TO ltmo;

--
-- Name: tagging_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE tagging_tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tagging_tag_id_seq OWNER TO ltmo;

--
-- Name: tagging_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE tagging_tag_id_seq OWNED BY tagging_tag.id;


--
-- Name: tagging_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('tagging_tag_id_seq', 69, true);


--
-- Name: tagging_taggeditem; Type: TABLE; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE TABLE tagging_taggeditem (
    id integer NOT NULL,
    tag_id integer NOT NULL,
    content_type_id integer NOT NULL,
    object_id integer NOT NULL,
    CONSTRAINT tagging_taggeditem_object_id_check CHECK ((object_id >= 0))
);


ALTER TABLE public.tagging_taggeditem OWNER TO ltmo;

--
-- Name: tagging_taggeditem_id_seq; Type: SEQUENCE; Schema: public; Owner: ltmo
--

CREATE SEQUENCE tagging_taggeditem_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MAXVALUE
    NO MINVALUE
    CACHE 1;


ALTER TABLE public.tagging_taggeditem_id_seq OWNER TO ltmo;

--
-- Name: tagging_taggeditem_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ltmo
--

ALTER SEQUENCE tagging_taggeditem_id_seq OWNED BY tagging_taggeditem.id;


--
-- Name: tagging_taggeditem_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ltmo
--

SELECT pg_catalog.setval('tagging_taggeditem_id_seq', 143, true);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE auth_message ALTER COLUMN id SET DEFAULT nextval('auth_message_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE ltmo_leak ALTER COLUMN id SET DEFAULT nextval('ltmo_leak_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE south_migrationhistory ALTER COLUMN id SET DEFAULT nextval('south_migrationhistory_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE tagging_tag ALTER COLUMN id SET DEFAULT nextval('tagging_tag_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: ltmo
--

ALTER TABLE tagging_taggeditem ALTER COLUMN id SET DEFAULT nextval('tagging_taggeditem_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_message; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY auth_message (id, user_id, message) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add message	4	add_message
11	Can change message	4	change_message
12	Can delete message	4	delete_message
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add tag	8	add_tag
23	Can change tag	8	change_tag
24	Can delete tag	8	delete_tag
25	Can add tagged item	9	add_taggeditem
26	Can change tagged item	9	change_taggeditem
27	Can delete tagged item	9	delete_taggeditem
28	Can add leak	10	add_leak
29	Can change leak	10	change_leak
30	Can delete leak	10	delete_leak
31	Can add log entry	11	add_logentry
32	Can change log entry	11	change_logentry
33	Can delete log entry	11	delete_logentry
34	Can add migration history	12	add_migrationhistory
35	Can change migration history	12	change_migrationhistory
36	Can delete migration history	12	delete_migrationhistory
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY auth_user (id, username, first_name, last_name, email, password, is_staff, is_active, is_superuser, last_login, date_joined) FROM stdin;
1	looser_magnus			loosingtoomuchoil@gmail.com	sha1$a6daa$9e9cfbe1685a77e6a40999b94c6af036782d2e13	t	t	t	2010-09-01 11:02:24.872511-03	2010-09-01 00:35:31.57274-03
3	etnalubma			francisco.herrero@gmail.com	sha1$eb48d$0f0ccd5d99a0b15121776b9676dd3403afd1961b	t	t	t	2010-09-29 14:36:48.402776-03	2010-09-01 00:37:41-03
2	tutuca			maturburu@gmail.com	sha1$0e662$6377b11c2e26bbd992eb76f54673b03e0cb05e19	t	t	t	2011-01-21 23:33:53.378882-03	2010-09-01 00:37:10-03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2010-09-01 11:03:44.965655-03	1	3	2	tutuca	2	Changed is_staff and is_superuser.
2	2010-09-01 11:03:54.978452-03	1	3	3	etnalubma	2	Changed is_staff and is_superuser.
3	2010-09-23 10:49:59.493642-03	2	10	65	etnalubma-apunto-lo-sorprendente-de-los-gi23084959	2	Changed description.
4	2010-09-23 10:51:05.94475-03	2	10	65	etnalubma-apunto-lo-sorprendente-de-los-gi23085105	2	Changed description.
5	2010-09-23 10:53:48.827539-03	2	10	65	etnalubma-apunto-lo-sorprendente-de-los-gi23085348	2	Changed description.
6	2010-09-26 11:15:15.093338-03	2	10	74	flash-y-la-recalcada-concha-de-tu-madre-25193317	3	
7	2010-09-26 13:23:05.397129-03	2	10	75	zsh-fail-ltmo_flasktu26112305	2	Changed description.
8	2010-09-26 13:24:06.157728-03	2	10	75	zsh-fail-ltmo_f26112406	2	Changed description.
9	2010-10-14 22:54:07.1691-03	2	10	87	Musiquita para compartir: Tierra adentro	2	Changed title, description and tags.
10	2011-01-21 23:34:20.670176-03	2	10	91	troll dance	2	Changed title and description.
11	2011-01-21 23:34:33.3498-03	2	10	80	STAR WARS VII	2	Changed title and description.
12	2011-01-21 23:47:59.91455-03	2	10	88	Anduve por el norte, anduve por el sur 	2	Changed title and description.
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	message	auth	message
5	content type	contenttypes	contenttype
6	session	sessions	session
7	site	sites	site
8	tag	tagging	tag
9	tagged item	tagging	taggeditem
10	leak	ltmo	leak
11	log entry	admin	logentry
12	migration history	south	migrationhistory
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
846df23bd69e0f39629a7c0703c3e9f9	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwF1LmU0ZjcxZmU4NmE5NWUzYmUwZDlh\nYjBmYjBlYmFmN2Nl\n	2010-09-15 11:02:25.008269-03
f09de84cb1d04b3e10e1b0423df4b856	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwN1LmEzZDIyNzVlZDE2MWM2YjliMTEx\nYjU3Njc0ODRjZDk1\n	2010-09-15 11:04:15.538818-03
95227f6a1ee65ee35cbb291f0b84619a	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwJ1LmU5MGJlZWFmY2UzYmI2ZGYxNmJj\nZDE0NjJkMzg3N2I0\n	2010-10-06 22:34:18.164237-03
4622ebe0afdbfcb7070acc35ab2aaa68	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwN1LmEzZDIyNzVlZDE2MWM2YjliMTEx\nYjU3Njc0ODRjZDk1\n	2010-10-13 14:36:48.759839-03
04d596190676a990feb8854308f2d1b5	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwJ1LmU5MGJlZWFmY2UzYmI2ZGYxNmJj\nZDE0NjJkMzg3N2I0\n	2010-10-28 22:53:13.922142-03
53175ff6d14b3f08b64e5a85bb90e361	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwJ1LmU5MGJlZWFmY2UzYmI2ZGYxNmJj\nZDE0NjJkMzg3N2I0\n	2010-11-17 11:27:55.417169-03
78deb9e8d4f9bf088b78dfcb9ad8c7f4	gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEESwJ1LmU5MGJlZWFmY2UzYmI2ZGYxNmJj\nZDE0NjJkMzg3N2I0\n	2011-02-04 23:33:53.421221-03
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY django_site (id, domain, name) FROM stdin;
1	localhost:8000	ltmo.com.ar
\.


--
-- Data for Name: ltmo_leak; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY ltmo_leak (id, slug, title, description, author, created, changed, tags, metadata, rendered) FROM stdin;
60	sin-titulo-20112032n	sin titulo	![entrada secreta](http://i.imgur.com/0FaNK.gif)\n	etnalubma	2010-09-10 12:02:04-03	2011-01-21 23:32:30.247728-03	gif,humor	{u'uptime': u'1 day, 1:48:14'}	<p><img alt="entrada secreta" src="http://i.imgur.com/0FaNK.gif" /></p>
5	sin-titulo-20112032n	sin titulo	![hola mundo](http://ltmo.com.ar)	anonymous	2010-08-24 12:07:20-03	2011-01-21 23:32:30.285277-03	r	{u'uptime': u'0 day, 2:25:39'}	<p><img alt="hola mundo" src="http://ltmo.com.ar" /></p>
10	no-20112032n	No	No	sancho	2010-08-24 13:53:08-03	2011-01-21 23:32:30.304902-03	test	{u'uptime': u'0 day, 0:49:55'}	<p>No</p>
38	war-what-is-it-good-for-abso-20112032n	War. What is it good for? Absolutly nothing (War - Edwin Starr)	**[War. What is it good for? Absolutly nothing](http://www.youtube.com/watch?v=_d8C4AIFgUg)** (War - Edwin Starr)\n\n	etnalubma	2010-08-27 14:33:38-03	2011-01-21 23:32:30.330105-03	video,edwin	{u'uptime': u'0 day, 4:30:22'}	<p><strong><a href="http://www.youtube.com/watch?v=_d8C4AIFgUg">War. What is it good for? Absolutly nothing</a></strong> (War - Edwin Starr)</p>
40	dos-links-sobre-bash-https-20112032n	Dos links sobre bash:\nhttp://sial.org/howto/shell/useless-cat/\nhttp://	Dos links sobre bash:\n\nhttp://sial.org/howto/shell/useless-cat/\n\nhttp://sial.org/howto/shell/\n\nPor supuesto pueden llegar al segundo desde el primero, pero me parecieron tan buenos que quería ponerlos explicitamente\n	tutuca	2010-08-28 20:42:13-03	2011-01-21 23:32:30.351686-03	bash,	{u'uptime': u'0 day, 3:20:15'}	<p>Dos links sobre bash:</p>\n<p>http://sial.org/howto/shell/useless-cat/</p>\n<p>http://sial.org/howto/shell/</p>\n<p>Por supuesto pueden llegar al segundo desde el primero, pero me parecieron tan buenos que quería ponerlos explicitamente</p>
42	impresionante-comercial-realiz-20112032n	Impresionante comercial realizado con Blender	[Impresionante comercial realizado con Blender](http://nachxs.wordpress.com/2010/08/29/impresionante-comercial-realizado-con-blender/)\n\n	mherrero	2010-08-29 11:18:34-03	2011-01-21 23:32:30.373785-03	blender	{u'uptime': u'0 day, 0:48:41'}	<p><a href="http://nachxs.wordpress.com/2010/08/29/impresionante-comercial-realizado-con-blender/">Impresionante comercial realizado con Blender</a></p>
43	sin-titulo-20112032n	sin titulo	![Alien Life Force](http://images.cheezburger.com/completestore/2010/8/27/ae3eae50-21a5-45f8-8af7-9eddc75caf73.gif)	etnalubma	2010-08-30 12:09:36-03	2011-01-21 23:32:30.394107-03	gif,animacion	{u'uptime': u'0 day, 1:34:14'}	<p><img alt="Alien Life Force" src="http://images.cheezburger.com/completestore/2010/8/27/ae3eae50-21a5-45f8-8af7-9eddc75caf73.gif" /></p>
44	esto-es-lo-que-pasa-cuando-fil-20112032n	Esto es lo que pasa cuando filmás las aspas de una avión con un celula	Esto es lo que pasa cuando filmás las aspas de una avión con un celular\nhttp://www.youtube.com/watch?v=LVwmtw\n	tutuca	2010-08-30 17:54:03-03	2011-01-21 23:32:30.416567-03	r	{u'uptime': u'0 day, 7:46:8'}	<p>Esto es lo que pasa cuando filmás las aspas de una avión con un celular\nhttp://www.youtube.com/watch?v=LVwmtw</p>
46	ya-asaltan-subestimer-20112032n	Ya-Asaltan Subestimer	[Ya-Asaltan Subestimer](http://www.youtube.com/watch?v=rL2EbVqgEyE)\n	fran	2010-08-31 14:58:19-03	2011-01-21 23:32:30.439002-03	video,chachacha	{u'uptime': u'0 day, 4:49:22'}	<p><a href="http://www.youtube.com/watch?v=rL2EbVqgEyE">Ya-Asaltan Subestimer</a></p>
47	el-almuerzo-20112032n	El almuerzo	[El almuerzo](http://web22.twitpic.com/img/154547713-bfec0d30d938a008ebe3bfd61eae182c.4c7d4320-full.jpg)\n	tutuca	2010-08-31 14:58:37-03	2011-01-21 23:32:30.46743-03	comida	{u'uptime': u'0 day, 0:8:27'}	<p><a href="http://web22.twitpic.com/img/154547713-bfec0d30d938a008ebe3bfd61eae182c.4c7d4320-full.jpg">El almuerzo</a></p>
48	mataria-poder-editar-los-derr-20112032n	\nMataría poder editar los derrames	![el almuerzo, corregido](http://imgur.com/HOf5A.jpg)\n\n\n\n\n\nMataría poder editar los derrames\n	tutuca	2010-08-31 16:19:02-03	2011-01-21 23:32:30.494967-03	r	{u'uptime': u'0 day, 1:28:54'}	<p><img alt="el almuerzo, corregido" src="http://imgur.com/HOf5A.jpg" /></p>\n<p>Mataría poder editar los derrames</p>
49	bash-15-interesantes-comandos-20112032n	bash: 15 interesantes comandos en una sola linea	bash: [15 interesantes comandos en una sola linea](http://lavidalinux.com.ar/2010/06/bash-15-interesantes-comandos-de-una-sola-linea.html)	fran	2010-09-01 12:09:24-03	2011-01-21 23:32:30.517378-03	bash,trucos	{u'uptime': u'1 day, 2:0:27'}	<p>bash: <a href="http://lavidalinux.com.ar/2010/06/bash-15-interesantes-comandos-de-una-sola-linea.html">15 interesantes comandos en una sola linea</a></p>
50	espera-siempre-lo-inesperado-20112032n	Espera siempre lo inesperado	[Espera siempre lo inesperado](http://www.youtube.com/watch?v=H70w_d9tuu0)	etnalubma	2010-09-02 00:47:04-03	2011-01-21 23:32:30.539663-03	video	{u'uptime': u'1 day, 14:38:7'}	<p><a href="http://www.youtube.com/watch?v=H70w_d9tuu0">Espera siempre lo inesperado</a></p>
51	sin-titulo-20112032n	sin titulo	![Never gonna give him out](http://i.imgur.com/ceCQw.jpg)\n	tutuca	2010-09-02 15:16:41-03	2011-01-21 23:32:30.561336-03	r	{u'uptime': u'0 day, 4:44:5'}	<p><img alt="Never gonna give him out" src="http://i.imgur.com/ceCQw.jpg" /></p>
54	el-inmortal-20112032n	El inmortal\n	El inmortal\n-----------\n![imagen](http://27.media.tumblr.com/tumblr_l2qn2vYfBG1qbk29ho1_500.jpg)	etnalubma	2010-09-04 02:46:51-03	2011-01-21 23:32:30.583607-03	foto,tiempo	{u'uptime': u'1 day, 14:13:42'}	<h2>El inmortal</h2>\n<p><img alt="imagen" src="http://27.media.tumblr.com/tumblr_l2qn2vYfBG1qbk29ho1_500.jpg" /></p>
55	que-sublimes-son-los-fractales-20112032n	Que sublimes son los fractales	[Que sublimes son los fractales](http://www.youtube.com/watch?v=iiXdzjdh6KA)\n	etnalubma	2010-09-04 14:21:58-03	2011-01-21 23:32:30.60668-03	video,fractales	{u'uptime': u'2 days, 1:48:22'}	<p><a href="http://www.youtube.com/watch?v=iiXdzjdh6KA">Que sublimes son los fractales</a></p>
57	perdi-mucho-aceite-cuando-qui-20112032n	Perdí mucho aceite, cuando quise hacer algo con los fluídos en Blender	Perdí mucho aceite, cuando quise hacer algo con los fluídos en Blender 2.5. No sabía que utilizar como modelo, entonces vino a mi auxilio LTMO. Este es el resultado [LTMO -01](http://www.youtube.com/watch?v=3ewBwiQ8GQ0) un pequeño video, anticipo de varios como homenaje a mi musa inspiradora.\n\n	mherrero	2010-09-06 13:31:01-03	2011-01-21 23:32:30.629439-03	blender,animacion,fluidos	{u'uptime': u'0 day, 3:16:20'}	<p>Perdí mucho aceite, cuando quise hacer algo con los fluídos en Blender 2.5. No sabía que utilizar como modelo, entonces vino a mi auxilio LTMO. Este es el resultado <a href="http://www.youtube.com/watch?v=3ewBwiQ8GQ0">LTMO -01</a> un pequeño video, anticipo de varios como homenaje a mi musa inspiradora.</p>
58	que-poronga-que-es-git-en-wind-20112032n	Que poronga que es git en windows	Que poronga que es git en windows	tutuca	2010-09-07 13:54:00-03	2011-01-21 23:32:30.649779-03	r	{u'uptime': u'1 day, 3:22:41'}	<p>Que poronga que es git en windows</p>
61	sin-titulo-20112032n	sin titulo	![Fireworks](http://fc03.deviantart.net/fs70/f/2010/136/9/6/Fire_Works____by_MattTheSamurai.gif)\n	etnalubma	2010-09-11 16:57:25-03	2011-01-21 23:32:30.671927-03	gif	{u'uptime': u'2 days, 6:43:15'}	<p><img alt="Fireworks" src="http://fc03.deviantart.net/fs70/f/2010/136/9/6/Fire_Works____by_MattTheSamurai.gif" /></p>
63	aaaaaa-aaa-a-ah-achuuusssss-20112032n	AAAAAA AAA A AH ACHUUUSSSSS\n	AAAAAA AAA A AH ACHUUUSSSSS\n==========================\n\n\n![Mierda con el resfrío](http://i.imgur.com/sJKY1.gif)\n	tutuca	2010-09-22 22:35:27-03	2011-01-21 23:32:30.720647-03	mierda	{u'uptime': u'0 day, 3:14:30'}	<h1>AAAAAA AAA A AH ACHUUUSSSSS</h1>\n<p><img alt="Mierda con el resfrío" src="http://i.imgur.com/sJKY1.gif" /></p>
64	oh-dios-mio-esta-lleno-de-20112032n	oh, Dios mio... esta lleno de estrellas	**[oh, Dios mio... esta lleno de estrellas](http://www.youtube.com/watch?v=ou6JNQwPWE0)**\n	etnalubma	2010-09-23 00:48:04-03	2011-01-21 23:32:30.752243-03	video,kurbic,2001	{u'uptime': u'0 day, 0:32:25'}	<p><strong><a href="http://www.youtube.com/watch?v=ou6JNQwPWE0">oh, Dios mio... esta lleno de estrellas</a></strong></p>
66	nothing-travels-faster-than-l-20112032n	"Nothing travels faster than light, with the possible exception of bad	"Nothing travels faster than light, with the possible exception of bad news, which follows its own rules." -Douglas Adams\n	tutuca	2010-09-23 10:29:33-03	2011-01-21 23:32:30.772589-03	frases	{u'uptime': u'0 day, 1:8:35'}	<p>"Nothing travels faster than light, with the possible exception of bad news, which follows its own rules." -Douglas Adams</p>
67	sin-titulo-20112032n	sin titulo	![fresh air](http://cheezpictureisunrelated.files.wordpress.com/2010/09/6c615fc4-fe4e-48dc-ad8d-a192ce2c5850.jpg)\n	etnalubma	2010-09-23 11:29:40-03	2011-01-21 23:32:30.809071-03	foto,unrelated	{u'uptime': u'0 day, 0:52:7'}	<p><img alt="fresh air" src="http://cheezpictureisunrelated.files.wordpress.com/2010/09/6c615fc4-fe4e-48dc-ad8d-a192ce2c5850.jpg" /></p>
68	sin-titulo-20112032n	sin titulo	![deja vu](http://bucket.lanacion.com.ar/anexos/fotos/15/1263715w590.JPG)\n	etnalubma	2010-09-23 14:12:15-03	2011-01-21 23:32:30.82088-03	liniers,historieta	{u'uptime': u'0 day, 3:35:1'}	<p><img alt="deja vu" src="http://bucket.lanacion.com.ar/anexos/fotos/15/1263715w590.JPG" /></p>
69	queremos-movernos-este-sitio-a-20112032n	Queremos movernos\nEste sitio actualmente está corriendo sobre django. 	Queremos movernos\n================\n\nEste sitio actualmente está corriendo sobre django. Lo cual nos permitió tenerlo andando bastante rápido considerando que:\n\n- Tenemos dos modelos muy simples y usamos la maquinaria built-in the autorizaciones.\n- Usamos los modelforms para validar los leaks, lo que nos permite evitar repetir el código de los modelos y los formularios, es especialmente útil para mantener los ForeignKeys (authors, tags).\n- Los RSS son una gilada, los mapas del sitio se hacen automáticos.\n- Los template tags de django son de las mejores cosas que hay.\n- Integrar comentarios al sitio es casi trivial.\n- El admin es zarpado. No lo usamos demasiado y podemos administrar todo desde la consola de python. Pero el admin es muy potente y viene gratis.\n\nHace un tiempo empecé a provar [flask](http://flask.pocoo.org/), el bichito viene bastante bonito. Es mucho más simple que django y en general parece más pythonico. Tengo listo un subset de prestaciones andando, en particular la lista de leaks y la publicación mediante spill. Sin embargo hay demasiadas cosas que quedan sin resolver:\n\n- No hay RSS, atom parece ser la posta entre la gente de pocoo, pero tampoco es taan simple ni tan potente como la solución que presta django.\n- No hay templatetags, aparentemente porque no las necesito. Ellos son más inteligentes que yo, así que deben estar en lo correcto.\n- No hay modelforms, ni formularios para el caso, así que si quiero validaciones automáticas o algo más o menos práctico tengo que intalar un paquete de terceras partes para esto (Casi todas son soluciones feas, como WTForms o FormAlchemy).\n- Tendría que implementar alguna solución para los comentarios (probablemente un proyecto en si mismo).\n- Tengo que implementar tags y alguna maquinaria parecida a [django-tagging](http://code.google.com/p/django-tagging/) por la mío. Probablemente también un proyecto en si mismo. Cosa que a su vez se hace más complejo por al cuestión de que no hay foreign keys automágicos.\n\nAsí que básicamente estoy llorando porque flask no es django, ya sé. No tengo apuro por migrar. Sin embargo trabajar con flask ha sido muy divertido hasta el momento y está tentador encarar los problemas más gruesos (tags, comentarios, forms). La comunidad es chica pero sólida y con ganas de que haya gente nueva, como siempre pasa en las comunidades chicas, pero con un poco de soberbia innecesaria. Parece siempre que si querés algo que el framework no provea (como querer agregarle funcionalidad al engine de templates sin tener que manosear la configuración del framework) en realidad estás haciendo las cosas mal y no necesitás lo que querés.\n\nEso me da un poco por las pelotas.\n\nAnyway. Estoy pensando en encarar esto sin apuro, pero con ganas. El código de ltmo está en el lugar habitual de github y [hay un branch](http://github.com/tutuca/ltmo/tree/flask-sql) que tiene las cosas que uso en flask. Voy a subir todo lo que haga a mi github y le ofrezco acceso como colaborador a cualquier interesado en encarar el desarrollo.\n\nTambién hay [algunos issues](http://github.com/tutuca/ltmo/issues) en general, que si nos dan una mano, sería groso.\n\nVamos a ver que nos depara el futuro. A derramar.\n\n	tutuca	2010-09-23 15:18:10-03	2011-01-21 23:32:30.853317-03	r	{u'uptime': u'0 day, 5:57:11'}	<h1>Queremos movernos</h1>\n<p>Este sitio actualmente está corriendo sobre django. Lo cual nos permitió tenerlo andando bastante rápido considerando que:</p>\n<ul>\n<li>Tenemos dos modelos muy simples y usamos la maquinaria built-in the autorizaciones.</li>\n<li>Usamos los modelforms para validar los leaks, lo que nos permite evitar repetir el código de los modelos y los formularios, es especialmente útil para mantener los ForeignKeys (authors, tags).</li>\n<li>Los RSS son una gilada, los mapas del sitio se hacen automáticos.</li>\n<li>Los template tags de django son de las mejores cosas que hay.</li>\n<li>Integrar comentarios al sitio es casi trivial.</li>\n<li>El admin es zarpado. No lo usamos demasiado y podemos administrar todo desde la consola de python. Pero el admin es muy potente y viene gratis.</li>\n</ul>\n<p>Hace un tiempo empecé a provar <a href="http://flask.pocoo.org/">flask</a>, el bichito viene bastante bonito. Es mucho más simple que django y en general parece más pythonico. Tengo listo un subset de prestaciones andando, en particular la lista de leaks y la publicación mediante spill. Sin embargo hay demasiadas cosas que quedan sin resolver:</p>\n<ul>\n<li>No hay RSS, atom parece ser la posta entre la gente de pocoo, pero tampoco es taan simple ni tan potente como la solución que presta django.</li>\n<li>No hay templatetags, aparentemente porque no las necesito. Ellos son más inteligentes que yo, así que deben estar en lo correcto.</li>\n<li>No hay modelforms, ni formularios para el caso, así que si quiero validaciones automáticas o algo más o menos práctico tengo que intalar un paquete de terceras partes para esto (Casi todas son soluciones feas, como WTForms o FormAlchemy).</li>\n<li>Tendría que implementar alguna solución para los comentarios (probablemente un proyecto en si mismo).</li>\n<li>Tengo que implementar tags y alguna maquinaria parecida a <a href="http://code.google.com/p/django-tagging/">django-tagging</a> por la mío. Probablemente también un proyecto en si mismo. Cosa que a su vez se hace más complejo por al cuestión de que no hay foreign keys automágicos.</li>\n</ul>\n<p>Así que básicamente estoy llorando porque flask no es django, ya sé. No tengo apuro por migrar. Sin embargo trabajar con flask ha sido muy divertido hasta el momento y está tentador encarar los problemas más gruesos (tags, comentarios, forms). La comunidad es chica pero sólida y con ganas de que haya gente nueva, como siempre pasa en las comunidades chicas, pero con un poco de soberbia innecesaria. Parece siempre que si querés algo que el framework no provea (como querer agregarle funcionalidad al engine de templates sin tener que manosear la configuración del framework) en realidad estás haciendo las cosas mal y no necesitás lo que querés.</p>\n<p>Eso me da un poco por las pelotas.</p>\n<p>Anyway. Estoy pensando en encarar esto sin apuro, pero con ganas. El código de ltmo está en el lugar habitual de github y <a href="http://github.com/tutuca/ltmo/tree/flask-sql">hay un branch</a> que tiene las cosas que uso en flask. Voy a subir todo lo que haga a mi github y le ofrezco acceso como colaborador a cualquier interesado en encarar el desarrollo.</p>\n<p>También hay <a href="http://github.com/tutuca/ltmo/issues">algunos issues</a> en general, que si nos dan una mano, sería groso.</p>\n<p>Vamos a ver que nos depara el futuro. A derramar.</p>
70	lo-que-es-visto-no-puede-ser-20112032n	lo que es visto, no puede ser des-visto\n\n	lo que es visto, no puede ser des-visto\n\n![Can't be unseen](http://www.dailyhaha.com/_pics/cannot_be_unseen.jpg)\n\n![KOALA](http://cdn1.knowyourmeme.com/i/000/042/045/original/1267641750554.jpg?1267642632)\n\n\n	tutuca	2010-09-24 11:58:27-03	2011-01-21 23:32:30.865641-03	r	{u'uptime': u'0 day, 3:36:5'}	<p>lo que es visto, no puede ser des-visto</p>\n<p><img alt="Can&apos;t be unseen" src="http://www.dailyhaha.com/_pics/cannot_be_unseen.jpg" /></p>\n<p><img alt="KOALA" src="http://cdn1.knowyourmeme.com/i/000/042/045/original/1267641750554.jpg?1267642632" /></p>
72	sin-titulo-20112032n	sin titulo	![fail text](http://failblog.files.wordpress.com/2010/09/13e52482-82ff-4cdb-bba4-4396e5dab837.jpg)\n	etnalubma	2010-09-24 15:23:01-03	2011-01-21 23:32:30.89994-03	foto,fail	{u'uptime': u'0 day, 5:24:37'}	<p><img alt="fail text" src="http://failblog.files.wordpress.com/2010/09/13e52482-82ff-4cdb-bba4-4396e5dab837.jpg" /></p>
73	sin-titulo-20112032n	sin titulo	![el barril del chavo](http://24.media.tumblr.com/tumblr_l99j8tBFIl1qbyk1so1_500.jpg)\n	etnalubma	2010-09-24 16:18:17-03	2011-01-21 23:32:30.927959-03	chavo,imagen	{u'uptime': u'0 day, 6:19:53'}	<p><img alt="el barril del chavo" src="http://24.media.tumblr.com/tumblr_l99j8tBFIl1qbyk1so1_500.jpg" /></p>
76	sin-titulo-20112032n	sin titulo	![panda punch](http://i.imgur.com/qURtX.gif\n)	etnalubma	2010-09-26 19:26:02-03	2011-01-21 23:32:30.983312-03	gif,panda,cafe	{u'uptime': u'1 day, 0:18:31'}	<p><img alt="panda punch" src="http://i.imgur.com/qURtX.gif" /></p>
77	sin-titulo-20112032n	sin titulo	![look_of_disaproval](http://i.imgur.com/go6IP.jpg)\n	tutuca	2010-09-27 17:30:40-03	2011-01-21 23:32:31.006728-03	gif,	{u'uptime': u'0 day, 12:15:52'}	<p><img alt="look_of_disaproval" src="http://i.imgur.com/go6IP.jpg" /></p>
78	sin-titulo-20112032n	sin titulo	![car crash](http://images.cheezburger.com/completestore/2010/9/27/865d64ed-e9b2-4ad2-974c-e9c0164bd0d8.gif)	etnalubma	2010-09-28 13:33:01-03	2011-01-21 23:32:31.027697-03	gif	{u'uptime': u'0 day, 14:3:4'}	<p><img alt="car crash" src="http://images.cheezburger.com/completestore/2010/9/27/865d64ed-e9b2-4ad2-974c-e9c0164bd0d8.gif" /></p>
79	cuando-la-luz-se-apaga-los-su-20112032n	Cuando la luz se apaga, los sueños se apoderan.	[Cuando la luz se apaga, los sueños se apoderan.](http://www.anasomnia.com/)	etnalubma	2010-09-29 00:29:57-03	2011-01-21 23:32:31.04967-03	sueños,flash,animacion	{u'uptime': u'0 day, 0:30:43'}	<p><a href="http://www.anasomnia.com/">Cuando la luz se apaga, los sueños se apoderan.</a></p>
81	disculpen-las-molestias-estam-20112032n	Disculpen las molestias. Estamos teniendo inconvenientes\n	Disculpen las molestias. Estamos teniendo inconvenientes\n![baby](http://images.cheezburger.com/completestore/2010/9/3/9ea6708b-ab61-4bcd-8780-02d23ed8a446.gif)	etnalubma	2010-10-01 17:34:59.684519-03	2011-01-21 23:32:31.076867-03	sorry	{u'uptime': u'2 days, 6:45:19'}	<p>Disculpen las molestias. Estamos teniendo inconvenientes\n<img alt="baby" src="http://images.cheezburger.com/completestore/2010/9/3/9ea6708b-ab61-4bcd-8780-02d23ed8a446.gif" /></p>
82	no-es-jackie-chan-20112032n	no es Jackie Chan	[no es Jackie Chan](http://www.youtube.com/watch?v=jbZnGk-q9kU)\n	etnalubma	2010-10-06 01:08:35.151441-03	2011-01-21 23:32:31.091139-03	videos	{u'uptime': u'0 day, 0:41:25'}	<p><a href="http://www.youtube.com/watch?v=jbZnGk-q9kU">no es Jackie Chan</a></p>
83	escribis-cualquier-cosa-aca-20112032n	Escribis cualquier cosa acá	Escribis cualquier cosa acá\n	tutuca	2010-10-06 22:43:34.459345-03	2011-01-21 23:32:31.109135-03	r	{u'uptime': u'0 day, 0:3:48'}	<p>Escribis cualquier cosa acá</p>
84	sigo-perdiendo-aceite-cua-20112032n	Sigo perdiendo aceite !!!! Cuando uso blender me aparece aceite en la 	*Sigo perdiendo aceite !!!!* Cuando uso blender me aparece aceite en la pantalla, ver video  [Alternative Energy Revolution](http://xkcd.com/556/) ![malla_plana_01]()\n![http://i111.photobucket.com/albums/n149/mherrero/Varios/0001.png]\n	anonymous	2010-10-08 00:21:06.133771-03	2011-01-21 23:32:31.121746-03	r	{u'uptime': u'0 day, 17:43:13'}	<p><em>Sigo perdiendo aceite !!!!</em> Cuando uso blender me aparece aceite en la pantalla, ver video  <a href="http://xkcd.com/556/">Alternative Energy Revolution</a> <img alt="malla_plana_01" src="" />\n![http://i111.photobucket.com/albums/n149/mherrero/Varios/0001.png]</p>
80	star-wars-vii-20112034n	STAR WARS VII	![vader country](http://www.b3tards.com/u/6c40fd723c102fa9fc71/thac.jpg)\r\nSTAR WARS VII\r\n=============\r\nVaderetro\r\n---------	etnalubma	2010-09-29 00:48:31-03	2011-01-21 23:34:33.343381-03	vader,foto	{u'uptime': u'0 day, 0:49:14'}	<p><img alt="vader country" src="http://www.b3tards.com/u/6c40fd723c102fa9fc71/thac.jpg" />\nSTAR WARS VII\n=============\nVaderetro</p>\n<hr />
86	sin-titulo-20112032n	sin titulo	![Los gatos son una masa](http://i.imgur.com/Wz3e9.gif)\n\n	tutuca	2010-10-12 14:22:24.277491-03	2011-01-21 23:32:31.142814-03	r	{u'uptime': u'0 day, 0:46:10'}	<p><img alt="Los gatos son una masa" src="http://i.imgur.com/Wz3e9.gif" /></p>
89	sin-titulo-20112032n	sin titulo	![Dance baby dance](http://i.imgur.com/uKFYb.gif)\n	tutuca	2010-11-09 08:49:00.649323-03	2011-01-21 23:32:31.217993-03	gif	{u'uptime': u'0 day, 12:46:8'}	<p><img alt="Dance baby dance" src="http://i.imgur.com/uKFYb.gif" /></p>
90	sin-titulo-20112032n	sin titulo	![Nothing to see here, move along](http://scienceblogs.com/startswithabang/upload/2010/07/dear_asteroid_hunters_stop_tel/nothing_to_see_here.jpg)\n	tutuca	2010-11-10 10:48:32.568215-03	2011-01-21 23:32:31.239065-03	r	{u'uptime': u'0 day, 0:8:18'}	<p><img alt="Nothing to see here, move along" src="http://scienceblogs.com/startswithabang/upload/2010/07/dear_asteroid_hunters_stop_tel/nothing_to_see_here.jpg" /></p>
88	anduve-por-el-norte-anduve-po-20112047n	Anduve por el norte, anduve por el sur 	Algunas cositas de Jericoacoara. Van a venir más :)\r\n\r\n![Ellos](http://farm5.static.flickr.com/4022/5142885312_e3909272ac.jpg)\r\n\r\n![Estrella Star](http://farm5.static.flickr.com/4126/5142888402_7a5e802d49.jpg)\r\n\r\n![Visitante](http://farm2.static.flickr.com/1355/5142893918_fe9096bff5.jpg)\r\n\r\n![Botin](http://farm2.static.flickr.com/1094/5142291051_5384f2f27a.jpg)\r\n\r\n\r\n	tutuca	2010-11-03 10:24:32.422291-03	2011-01-21 23:47:59.908502-03	read	{u'uptime': u'0 day, 0:33:23'}	<p>Algunas cositas de Jericoacoara. Van a venir más :)</p>\n<p><img alt="Ellos" src="http://farm5.static.flickr.com/4022/5142885312_e3909272ac.jpg" /></p>\n<p><img alt="Estrella Star" src="http://farm5.static.flickr.com/4126/5142888402_7a5e802d49.jpg" /></p>\n<p><img alt="Visitante" src="http://farm2.static.flickr.com/1355/5142893918_fe9096bff5.jpg" /></p>\n<p><img alt="Botin" src="http://farm2.static.flickr.com/1094/5142291051_5384f2f27a.jpg" /></p>
92	sin-titulo-20112032n	sin titulo	![Videla y Menedez desfilando en tanga por el paredón](http://www.pagina12.com.ar/fotos/20101224/rudypaz/na01di01.gif)\n	tutuca	2010-12-26 00:58:11.662223-03	2011-01-21 23:32:31.283894-03	videla,	{u'uptime': u'0 day, 1:6:27'}	<p><img alt="Videla y Menedez desfilando en tanga por el paredón" src="http://www.pagina12.com.ar/fotos/20101224/rudypaz/na01di01.gif" /></p>
6	sin-titulo-20112032n	sin titulo	![Firefox has crashed into jaws](http://images.cheezburger.com/completestore/2010/8/21/d4f9115d-7677-4819-aa18-b847484b1cdd.gif)	anonymous	2010-08-24 12:08:52-03	2011-01-21 23:32:31.307105-03	gif	{u'uptime': u'0 day, 2:27:12'}	<p><img alt="Firefox has crashed into jaws" src="http://images.cheezburger.com/completestore/2010/8/21/d4f9115d-7677-4819-aa18-b847484b1cdd.gif" /></p>
7	sin-titulo-20112032n	sin titulo	![EWOCK is friendly](http://gallery.wimetal.org/d/555-2/ewok.gif)	anonymous	2010-08-24 12:24:27-03	2011-01-21 23:32:31.327869-03	gif	{u'uptime': u'0 day, 2:42:46'}	<p><img alt="EWOCK is friendly" src="http://gallery.wimetal.org/d/555-2/ewok.gif" /></p>
15	sin-titulo-20112032n	sin titulo	![happy house](http://images.cheezburger.com/completestore/2010/8/17/2ea3d277-e6a2-477e-bacf-06a267d9b265.gif)	etnalubma	2010-08-24 15:16:49-03	2011-01-21 23:32:31.350277-03	gif	{u'uptime': u'0 day, 5:35:8'}	<p><img alt="happy house" src="http://images.cheezburger.com/completestore/2010/8/17/2ea3d277-e6a2-477e-bacf-06a267d9b265.gif" /></p>
33	sin-titulo-20112032n	sin titulo	![¿Donde esta Oesterheld?](http://i111.photobucket.com/albums/n149/mherrero/varios/aficheOesterheld.jpg)\n	mherrero	2010-08-26 22:28:32-03	2011-01-21 23:32:31.372878-03	oesterheld	{u'uptime': u'0 day, 13:12:30'}	<p><img alt="¿Donde esta Oesterheld?" src="http://i111.photobucket.com/albums/n149/mherrero/varios/aficheOesterheld.jpg" /></p>
8	si-tuviera-un-fin-donde-esta-20112032n	Si tuviera un fin, ¿donde esta el misterio?	*Si tuviera un fin, ¿donde esta el misterio?*	anonymous	2010-08-24 12:59:15-03	2011-01-21 23:32:31.395238-03	frase	{u'uptime': u'0 day, 3:40:31'}	<p><em>Si tuviera un fin, ¿donde esta el misterio?</em></p>
9	por-favor-sea-amable-20112032n	Por favor, sea amable. 	*Por favor, sea amable.* ![trollface](http://images.whatport80.com/images/thumb/c/cf/Trollface.jpg/400px-Trollface.jpg)	anonymous	2010-08-24 13:03:26-03	2011-01-21 23:32:31.412844-03	frase	{u'uptime': u'0 day, 3:44:35'}	<p><em>Por favor, sea amable.</em> <img alt="trollface" src="http://images.whatport80.com/images/thumb/c/cf/Trollface.jpg/400px-Trollface.jpg" /></p>
11	no-sabia-que-decir-hasta-que-m-20112032n	No sabia que decir hasta que me di cuenta que estaba perdiendo aceite 	No sabia que decir hasta que me di cuenta que estaba perdiendo aceite pensando que mandar solo para probar que esto anda.\n	sancho	2010-08-24 13:54:26-03	2011-01-21 23:32:31.437319-03	test	{u'uptime': u'0 day, 0:51:6'}	<p>No sabia que decir hasta que me di cuenta que estaba perdiendo aceite pensando que mandar solo para probar que esto anda.</p>
12	que-no-te-hayamos-dicho-las-r-20112032n	\nQue no te hayamos dicho las razones no quiere decir que no las haya\n	> Que no te hayamos dicho las razones no quiere decir que no las haya	pandres	2010-08-24 14:14:52-03	2011-01-21 23:32:31.461344-03	frases	{u'uptime': u'0 day, 4:33:11'}	<blockquote>\n<p>Que no te hayamos dicho las razones no quiere decir que no las haya</p>\n</blockquote>
13	instalando-django-solr-varni-20112032n	instalando Django, Solr, Varnish y Supervisord en un buildout	[instalando Django, Solr, Varnish y Supervisord en un buildout](http://zebert.blogspot.com/2009/05/installing-django-solr-varnish-and.html)	etnalubma	2010-08-24 14:38:57-03	2011-01-21 23:32:31.477343-03	solr,python,buildout,django,varnish,supervisord	{u'uptime': u'0 day, 5:20:14'}	<p><a href="http://zebert.blogspot.com/2009/05/installing-django-solr-varnish-and.html">instalando Django, Solr, Varnish y Supervisord en un buildout</a></p>
14	silent-bob-dancing-20112032n	!silent bob dancing	\\![silent bob dancing](http://images.cheezburger.com/completestore/2010/8/22/06582b04-ec10-46a6-930e-11aa5798ad5a.gif)	etnalubma	2010-08-24 15:00:47-03	2011-01-21 23:32:31.488034-03	gif	{u'uptime': u'0 day, 5:42:4'}	<p>!<a href="http://images.cheezburger.com/completestore/2010/8/22/06582b04-ec10-46a6-930e-11aa5798ad5a.gif">silent bob dancing</a></p>
91	troll-dance-20112034n	troll dance	![Troll dance]([http://i.imgur.com/Emi0l.gif)\r\n	tutuca	2010-12-08 18:50:53.675697-03	2011-01-21 23:34:20.663868-03	gif	{u'uptime': u'0 day, 3:33:49'}	<p><img alt="Troll dance" src="[http://i.imgur.com/Emi0l.gif" /></p>
16	httpwwwyoutubecomwatchv-20112032n	http://www.youtube.com/watch?v=uPVHjkMS5vU	http://www.youtube.com/watch?v=uPVHjkMS5vU\n	sancho	2010-08-24 15:37:25-03	2011-01-21 23:32:31.49857-03	gorilas	{u'uptime': u'0 day, 2:34:15'}	<p>http://www.youtube.com/watch?v=uPVHjkMS5vU</p>
18	house-era-re-groso-como-rapero-20112032n	House era re groso como rapero....... Para ser inglés, http://www.yout	House era re groso como rapero....... Para ser inglés, http://www.youtube.com/watch?v=XdRfhARwGoI	anonymous	2010-08-24 20:10:03-03	2011-01-21 23:32:31.523-03	videito,	{u'uptime': u'0 day, 10:28:22'}	<p>House era re groso como rapero....... Para ser inglés, http://www.youtube.com/watch?v=XdRfhARwGoI</p>
19	una-manana-iluminada-con-400-b-20112032n	Una mañana iluminada con 400 billones de soles	[Una mañana iluminada con 400 billones de soles](http://www.youtube.com/watch?v=zSgiXGELjbc)	etnalubma	2010-08-25 01:06:30-03	2011-01-21 23:32:31.550034-03	sagan,video	{u'uptime': u'0 day, 0:41:2'}	<p><a href="http://www.youtube.com/watch?v=zSgiXGELjbc">Una mañana iluminada con 400 billones de soles</a></p>
20	somos-un-medio-para-el-cosmos-20112032n	Somos un medio para el Cosmos de conocerse a sí mismo (Carl Sagan)	*Somos un medio para el Cosmos de conocerse a sí mismo* (Carl Sagan)	etnalubma	2010-08-25 14:14:03-03	2011-01-21 23:32:31.573014-03	frase,sagan	{u'uptime': u'0 day, 3:52:11'}	<p><em>Somos un medio para el Cosmos de conocerse a sí mismo</em> (Carl Sagan)</p>
25	probando-nuevamente-le-agregue-20112032n	Probando nuevamente\nLe agregué la capacidad de usar un editor de texto	Probando nuevamente\n==============\n\nLe agregué la capacidad de usar un editor de texto a spill y no se que onda.\n\nEspero que ande bien\n	tutuca	2010-08-26 12:45:59-03	2011-01-21 23:32:31.596349-03	pruebas	{u'uptime': u'0 day, 1:41:15'}	<h1>Probando nuevamente</h1>\n<p>Le agregué la capacidad de usar un editor de texto a spill y no se que onda.</p>\n<p>Espero que ande bien</p>
26	weeee-anda-de-lujo-esto-se-v-20112032n	WEEEE, anda de lujo\n\nEsto se va para arriba. Me sorprende todo lo que 	WEEEE, anda de lujo\n============\n\n![Aguante ](http://chzgifs.files.wordpress.com/2010/06/rickroll.gif)\n\nEsto se va para arriba. Me sorprende todo lo que se puede avanzar en los ratos libres.\n\n	tutuca	2010-08-26 13:03:35-03	2011-01-21 23:32:31.619502-03	pruebas,	{u'uptime': u'0 day, 1:58:50'}	<h1>WEEEE, anda de lujo</h1>\n<p><img alt="Aguante " src="http://chzgifs.files.wordpress.com/2010/06/rickroll.gif" /></p>\n<p>Esto se va para arriba. Me sorprende todo lo que se puede avanzar en los ratos libres.</p>
27	asdfasdf-sadfasdfas-df-20112032n	asdfasdf\nsadfasdfas\ndf	asdfasdf\nsadfasdfas\ndf\n\n\n	etnalubma	2010-08-26 13:06:24-03	2011-01-21 23:32:31.637067-03	prueba	{u'uptime': u'0 day, 3:5:59'}	<p>asdfasdf\nsadfasdfas\ndf</p>
28	que-tan-jodida-es-mi-base-de-d-20112032n	Que tan jodida es mi base de datos\nAcá usamos postgres para producción	[Que tan jodida es mi base de datos](http://howfuckedismydatabase.com)\n\nAcá usamos postgres para producción y sqlite para desarrollo así que andamos bien ;-)\n	anonymous	2010-08-26 15:01:39-03	2011-01-21 23:32:31.664015-03	r	{u'uptime': u'0 day, 3:56:54'}	<p><a href="http://howfuckedismydatabase.com">Que tan jodida es mi base de datos</a></p>\n<p>Acá usamos postgres para producción y sqlite para desarrollo así que andamos bien ;-)</p>
29	aparentemente-no-tan-jodida-co-20112032n	Aparentemente no tan jodida como el parser de markdown2	Aparentemente no tan jodida como el parser de markdown2\n	tutuca	2010-08-26 15:20:23-03	2011-01-21 23:32:31.683725-03	giladas	{u'uptime': u'0 day, 4:15:39'}	<p>Aparentemente no tan jodida como el parser de markdown2</p>
31	no-entiendo-esta-parte-del-edi-20112032n	No entiendo esta parte del editor de texto?	No entiendo esta parte del editor de texto?\n	mherrero	2010-08-26 21:41:27-03	2011-01-21 23:32:31.727652-03	test	{u'uptime': u'0 day, 12:25:24'}	<p>No entiendo esta parte del editor de texto?</p>
32	en-el-test-anterior-estaba-per-20112032n	En el test anterior estaba perdiendo aceite, ahora entiendo. Solo se p	En el test anterior estaba perdiendo aceite, ahora entiendo. Solo se pone así python spill -t test -a mherrero enter al procesador de texto, luego control X y aleluya ya esta en pantalla en el fabuloso *LTMO*\n	mherrero	2010-08-26 21:49:59-03	2011-01-21 23:32:31.751367-03	test	{u'uptime': u'0 day, 12:33:52'}	<p>En el test anterior estaba perdiendo aceite, ahora entiendo. Solo se pone así python spill -t test -a mherrero enter al procesador de texto, luego control X y aleluya ya esta en pantalla en el fabuloso <em>LTMO</em></p>
34	sin-titulo-20112032n	sin titulo	![¿Donde esta Oesterheld?](http://i111.photobucket.com/albums/n149/mherrero/Varios/aficheOesterheld.jpg)\n	mherrero	2010-08-26 22:31:02-03	2011-01-21 23:32:31.772972-03	oesterheld	{u'uptime': u'0 day, 13:14:55'}	<p><img alt="¿Donde esta Oesterheld?" src="http://i111.photobucket.com/albums/n149/mherrero/Varios/aficheOesterheld.jpg" /></p>
35	ponga-su-spill-mas-a-mano-en-l-20112032n	Ponga su spill mas a mano en Linux\nAgregue estas lineas al bashrc:\nali	Ponga su spill mas a mano en Linux\n----------------------------------\nAgregue estas lineas al bashrc:\n\n`alias spill="~/repositorio/bin/spill.py"\nexport editor="vim" # o nano, emacs, vi, mcedit, gedit`\n\ny disfrute de la sensación de derramar aceite.\n	etnalubma	2010-08-27 10:56:38-03	2011-01-21 23:32:31.798667-03	codigo,trucos,spill	{u'uptime': u'0 day, 0:53:2'}	<h2>Ponga su spill mas a mano en Linux</h2>\n<p>Agregue estas lineas al bashrc:</p>\n<p><code>alias spill="~/repositorio/bin/spill.py"\nexport editor="vim" # o nano, emacs, vi, mcedit, gedit</code></p>\n<p>y disfrute de la sensación de derramar aceite.</p>
36	pronto-tendremos-videitos-embe-20112032n	Pronto tendremos videitos embebidos con esto	Pronto tendremos videitos embebidos con **[esto](http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/)**\n	etnalubma	2010-08-27 11:00:33-03	2011-01-21 23:32:31.830293-03	codigo,trucos,spill	{u'uptime': u'0 day, 0:56:54'}	<p>Pronto tendremos videitos embebidos con <strong><a href="http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/">esto</a></strong></p>
4	buenos-datos-sobre-seo-es-un-20112032n	Buenos datos sobre SEO, es un poco básico pero no deja se ser interesa	Buenos datos sobre SEO, es un poco básico pero no deja se ser interesante http://www.seomoz.org/blog/a-comprehensive-intro-to-seo-powerpoint-slide-deck- 	rafen	2010-08-24 12:02:17-03	2011-01-21 23:32:31.85062-03	seo,	{u'uptime': u'0 day, 2:20:35'}	<p>Buenos datos sobre SEO, es un poco básico pero no deja se ser interesante http://www.seomoz.org/blog/a-comprehensive-intro-to-seo-powerpoint-slide-deck- </p>
62	el-secdleto-de-la-tlompeta-es-20112032n	El secdleto de la tlompeta\n\nEs un corto producido por Javier Fresser,\n	El secdleto de la tlompeta\n--------------------------\n![telefonia](http://3.bp.blogspot.com/_y2yg9JIjH8k/Szs6-QgMXII/AAAAAAAABzA/SG-Ci7mvE_M/s320/secdleto1.JPG)\n\nEs un corto producido por [Javier Fresser](http://es.wikipedia.org/wiki/Javier_Fesser),\nconocido por dirigir **El Milagro de P. Tinto** y **La gran aventura de Mortadelo y Filemon**.\nNo tiene desperdicio.\n\nLa pueden ver [aquí](http://video.google.es/videoplay?docid=465464602026455980)	etnalubma	2010-09-15 17:25:28-03	2011-01-21 23:32:30.701676-03	video,javier fresser	{u'uptime': u'0 day, 6:52:32'}	<h2>El secdleto de la tlompeta</h2>\n<p><img alt="telefonia" src="http://3.bp.blogspot.com/_y2yg9JIjH8k/Szs6-QgMXII/AAAAAAAABzA/SG-Ci7mvE_M/s320/secdleto1.JPG" /></p>\n<p>Es un corto producido por <a href="http://es.wikipedia.org/wiki/Javier_Fesser">Javier Fresser</a>,\nconocido por dirigir <strong>El Milagro de P. Tinto</strong> y <strong>La gran aventura de Mortadelo y Filemon</strong>.\nNo tiene desperdicio.</p>\n<p>La pueden ver <a href="http://video.google.es/videoplay?docid=465464602026455980">aquí</a></p>
1	dolor-sit-amet-consecteuter-no-20112032n	Dolor sit amet consecteuter nomi	Dolor sit amet consecteuter nomi\r\n	tutuca	2010-09-28 21:44:52-03	2011-01-21 23:32:31.921498-03	r	{u'uptime': u'0 day, 1:43:42'}	<p>Dolor sit amet consecteuter nomi</p>
3	probando-como-anda-este-coso-20112032n	Probando como anda este coso. Tratando de hacerlo mejor, que deje dese	Probando como anda este coso. Tratando de hacerlo mejor, que deje deser una suma de azar, más bien resultado de los azahares\r\n	tutuca	2010-09-28 22:11:38-03	2011-01-21 23:32:31.943268-03	r	{u'uptime': u'0 day, 2:10:28'}	<p>Probando como anda este coso. Tratando de hacerlo mejor, que deje deser una suma de azar, más bien resultado de los azahares</p>
39	como-usar-caracteres-letras-20112032n	Como usar caracteres (letras) compuestas en linux\nhttp://www.reddit.co	Como usar caracteres (letras) compuestas en linux\n\nhttp://www.reddit.com/r/linux/comments/ch61l/\n\nNo sabía que había tantas, particularmente estaba buscando el de look of disaproval o sea ಠ pero no encontré lo que quería.\n	tutuca	2010-08-28 19:38:58-03	2011-01-21 23:32:31.955045-03	r	{u'uptime': u'0 day, 2:17:0'}	<p>Como usar caracteres (letras) compuestas en linux</p>\n<p>http://www.reddit.com/r/linux/comments/ch61l/</p>\n<p>No sabía que había tantas, particularmente estaba buscando el de look of disaproval o sea ಠ pero no encontré lo que quería.</p>
41	este-es-un-gif-animado-hecho-a-20112032n	Este es un gif animado hecho a partir de una animación hecha con Blend	Este es un gif animado hecho a partir de una animación hecha con Blender, pierde aceite por todos lados igual que LTMO.\n![](http://s111.photobucket.com/albums/n149/mherrero/Varios/LTMO_200.gif)\n![](http://s111.photobucket.com/albums/n149/mherrero/Varios/LTMO_400.gif)\n\n	mherrero	2010-08-28 22:56:37-03	2011-01-21 23:32:31.975906-03	gif,animacion,blender	{u'uptime': u'0 day, 3:15:43'}	<p>Este es un gif animado hecho a partir de una animación hecha con Blender, pierde aceite por todos lados igual que LTMO.\n<img alt="" src="http://s111.photobucket.com/albums/n149/mherrero/Varios/LTMO_200.gif" />\n<img alt="" src="http://s111.photobucket.com/albums/n149/mherrero/Varios/LTMO_400.gif" /></p>
52	you-took-too-much-man-you-took-20112032n	You took too much man\nYou took too much, too much	You took too much man\n====================\n\nYou took too much, too much\n===================\n	tutuca	2010-09-02 20:52:50-03	2011-01-21 23:32:32.029441-03	frases	{u'uptime': u'0 day, 10:20:14'}	<h1>You took too much man</h1>\n<h1>You took too much, too much</h1>
53	san-martin-debian-peron-lib-20112032n	San Martín, Debian, Perón. Libertad para el pueblo	[San Martín, Debian, Perón. Libertad para el pueblo](http://evitalinuxera.blogspot.com/2010/08/san-martin-debian-peron-libertad-para.html)	etnalubma	2010-09-03 11:28:05-03	2011-01-21 23:32:32.052151-03	peron,san martin,debian,linux	{u'uptime': u'0 day, 22:54:29'}	<p><a href="http://evitalinuxera.blogspot.com/2010/08/san-martin-debian-peron-libertad-para.html">San Martín, Debian, Perón. Libertad para el pueblo</a></p>
56	historia-de-un-linuxero-que-mi-20112032n	Historia de un Linuxero que migra a Windows\nmherrero nos recomendó est	Historia de un Linuxero que migra a Windows\n-------------------------------------------\n\nmherrero nos recomendó esta interesante historia, que nos introduce en una forma distinta\nde pensar el problema de usar Windows.\n\n*[ver artículo](http://libertadzero.wordpress.com/2010/09/06/historia-de-un-linuxero-que-migra-a-windows/)*	etnalubma	2010-09-06 13:29:02-03	2011-01-21 23:32:32.067512-03	linux,windows,articulo	{u'uptime': u'0 day, 21:36:57'}	<h2>Historia de un Linuxero que migra a Windows</h2>\n<p>mherrero nos recomendó esta interesante historia, que nos introduce en una forma distinta\nde pensar el problema de usar Windows.</p>\n<p><em><a href="http://libertadzero.wordpress.com/2010/09/06/historia-de-un-linuxero-que-migra-a-windows/">ver artículo</a></em></p>
59	siempre-aparece-don-quijote-l-20112032n	Siempre aparece Don Quijote, lastima que uno sea un Sancho Panza !!!! 	*Siempre aparece Don Quijote, lastima que uno sea un Sancho Panza !!!!*  [Alternative Energy Revolution](http://xkcd.com/556/) ![Alternative Energy Revolution](http://imgs.xkcd.com/comics/alternative_energy_revolution.jpg)\n	mherrero	2010-09-08 11:56:41-03	2011-01-21 23:32:32.088999-03	humor	{u'uptime': u'0 day, 2:25:50'}	<p><em>Siempre aparece Don Quijote, lastima que uno sea un Sancho Panza !!!!</em>  <a href="http://xkcd.com/556/">Alternative Energy Revolution</a> <img alt="Alternative Energy Revolution" src="http://imgs.xkcd.com/comics/alternative_energy_revolution.jpg" /></p>
65	etnalubma-apunto-lo-sorprenden-20112032n	etnalubma apuntó lo sorprendente de los gif animados últimamente. Cómo	etnalubma apuntó lo sorprendente de los gif animados últimamente. Cómo han recuperado valor.\r\n\r\nMe hizo acordar a esta [charla de Lawrence Lessig](http://www.ted.com/talks/larry_lessig_says_the_law_is_strangling_creativity.html). El significado cultural del remix.\r\n\r\nUn groso el vago.	tutuca	2010-09-23 01:02:11-03	2011-01-21 23:32:30.797692-03	charlas,	{u'uptime': u'0 day, 5:41:8'}	<p>etnalubma apuntó lo sorprendente de los gif animados últimamente. Cómo han recuperado valor.</p>\n<p>Me hizo acordar a esta <a href="http://www.ted.com/talks/larry_lessig_says_the_law_is_strangling_creativity.html">charla de Lawrence Lessig</a>. El significado cultural del remix.</p>\n<p>Un groso el vago.</p>
71	burbujas-burbujas-por-todos-l-20112032n	Burbujas, burbujas por todos lados\n\n	Burbujas, burbujas por todos lados\n\n![Burbuja](http://farm3.static.flickr.com/2494/3673992165_b89e6eedc8_o.jpg)\n\n![Burbuja](http://farm4.static.flickr.com/3037/3674813550_d8f62e3149_o.jpg )\n\n\n	tutuca	2010-09-24 14:37:23-03	2011-01-21 23:32:30.878377-03	decara	{u'uptime': u'0 day, 6:15:0'}	<p>Burbujas, burbujas por todos lados</p>\n<p><img alt="Burbuja" src="http://farm3.static.flickr.com/2494/3673992165_b89e6eedc8_o.jpg" /></p>\n<p><img alt="Burbuja" src="http://farm4.static.flickr.com/3037/3674813550_d8f62e3149_o.jpg" /></p>
75	zsh-fail-ltmo_flasktut-20112032n	zsh Fail:\n    (ltmo_flask)[tutuca@gatonegro ltmo]\\$ pip install ipytho	zsh Fail:\r\n============\r\n\r\n        (ltmo_flask)[tutuca@gatonegro ltmo]\\$ pip install ipython\r\n        Downloading/unpacking ipython\r\n        Downloading ipython-0.10.tar.gz (5.8Mb): 5.8Mb downloaded\r\n        Running setup.py egg_info for package ipython\r\n        Installing collected packages: ipython\r\n        Running setup.py install for ipython\r\n        Installing iptest script to /home/tutuca/venvs/ltmo_flask/bin\r\n        Installing ipythonx script to /home/tutuca/venvs/ltmo_flask/bin\r\n        Installing ipcluster script to /home/tutuca/venvs/ltmo_flask/bin\r\n        Installing ipython script to /home/tutuca/venvs/ltmo_flask/bin\r\n        Installing pycolor script to /home/tutuca/venvs/ltmo_flask/bin\r\n        Installing ipcontroller script to /home/tutuca/venvs/ltmo_flask/bin\r\n        Installing ipengine script to /home/tutuca/venvs/ltmo_flask/bin\r\n        *Successfully installed ipython*\r\n        (ltmo_flask)[tutuca@gatonegro ltmo]\\$ ipython\r\n        Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)\r\n        Type "copyright", "credits" or "license" for more information.\r\n\r\n        IPython 0.10 -- An enhanced Interactive Python.\r\n        ?         -> Introduction and overview of IPython's features.\r\n        %quickref -> Quick reference.\r\n        help      -> Python's own help system.\r\n        object?   -> Details about 'object'. ?object also works, ?? prints more.\r\n\r\n        In [1]: from ltmo.models import Leak\r\n        ---------------------------------------------------------------------------\r\n        ImportError                               Traceback (most recent call last)\r\n\r\n        /home/tutuca/Proyectos/ltmo/<ipython console> in <module>()\r\n\r\n        /home/tutuca/Proyectos/ltmo/ltmo/__init__.py in <module>()\r\n              4 import json\r\n              5 import settings\r\n        ----> 6 from flask import Flask\r\n              7 from flask import request, session, g, redirect, url_for, render_template, flash\r\n              8 from flaskext.markdown import Markdown\r\n\r\n        ImportError: No module named flask\r\n\r\n        In [2]: import flask\r\n        ---------------------------------------------------------------------------\r\n        ImportError                               Traceback (most recent call last)\r\n\r\n        /home/tutuca/Proyectos/ltmo/<ipython console> in <module>()\r\n\r\n        ImportError: No module named flask\r\n\r\n        In [3]:\r\n        Do you really want to exit ([y]/n)?\r\n        (ltmo_flask)[tutuca@gatonegro ltmo]\\$ which ipython\r\n        /usr/local/bin/ipython\r\n        (ltmo_flask)[tutuca@gatonegro ltmo]\\$ deactivate\r\n        [tutuca@gatonegro ltmo]\\$ . ~/bin/ltmo\r\n        (ltmo_flask)[tutuca@gatonegro ltmo]\\$ iptyhon\r\n        *zsh: command not found: iptyhon*\r\n        (ltmo_flask)[tutuca@gatonegro ltmo]\\$\r\n\r\n	tutuca	2010-09-26 13:22:22-03	2011-01-21 23:32:30.953327-03	python,	{u'uptime': u'0 day, 3:45:56'}	<h1>zsh Fail:</h1>\n<pre><code>    (ltmo_flask)[tutuca@gatonegro ltmo]\\$ pip install ipython\n    Downloading/unpacking ipython\n    Downloading ipython-0.10.tar.gz (5.8Mb): 5.8Mb downloaded\n    Running setup.py egg_info for package ipython\n    Installing collected packages: ipython\n    Running setup.py install for ipython\n    Installing iptest script to /home/tutuca/venvs/ltmo_flask/bin\n    Installing ipythonx script to /home/tutuca/venvs/ltmo_flask/bin\n    Installing ipcluster script to /home/tutuca/venvs/ltmo_flask/bin\n    Installing ipython script to /home/tutuca/venvs/ltmo_flask/bin\n    Installing pycolor script to /home/tutuca/venvs/ltmo_flask/bin\n    Installing ipcontroller script to /home/tutuca/venvs/ltmo_flask/bin\n    Installing ipengine script to /home/tutuca/venvs/ltmo_flask/bin\n    *Successfully installed ipython*\n    (ltmo_flask)[tutuca@gatonegro ltmo]\\$ ipython\n    Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)\n    Type "copyright", "credits" or "license" for more information.\n\n    IPython 0.10 -- An enhanced Interactive Python.\n    ?         -&gt; Introduction and overview of IPython's features.\n    %quickref -&gt; Quick reference.\n    help      -&gt; Python's own help system.\n    object?   -&gt; Details about 'object'. ?object also works, ?? prints more.\n\n    In [1]: from ltmo.models import Leak\n    ---------------------------------------------------------------------------\n    ImportError                               Traceback (most recent call last)\n\n    /home/tutuca/Proyectos/ltmo/&lt;ipython console&gt; in &lt;module&gt;()\n\n    /home/tutuca/Proyectos/ltmo/ltmo/__init__.py in &lt;module&gt;()\n          4 import json\n          5 import settings\n    ----&gt; 6 from flask import Flask\n          7 from flask import request, session, g, redirect, url_for, render_template, flash\n          8 from flaskext.markdown import Markdown\n\n    ImportError: No module named flask\n\n    In [2]: import flask\n    ---------------------------------------------------------------------------\n    ImportError                               Traceback (most recent call last)\n\n    /home/tutuca/Proyectos/ltmo/&lt;ipython console&gt; in &lt;module&gt;()\n\n    ImportError: No module named flask\n\n    In [3]:\n    Do you really want to exit ([y]/n)?\n    (ltmo_flask)[tutuca@gatonegro ltmo]\\$ which ipython\n    /usr/local/bin/ipython\n    (ltmo_flask)[tutuca@gatonegro ltmo]\\$ deactivate\n    [tutuca@gatonegro ltmo]\\$ . ~/bin/ltmo\n    (ltmo_flask)[tutuca@gatonegro ltmo]\\$ iptyhon\n    *zsh: command not found: iptyhon*\n    (ltmo_flask)[tutuca@gatonegro ltmo]\\$\n</code></pre>
85	sin-titulo-20112032n	sin titulo	![AMIGAAAAA](http://i.imgur.com/vlBaR.jpg)\n	tutuca	2010-10-12 14:12:12.904904-03	2011-01-21 23:32:31.131794-03	r	{u'uptime': u'0 day, 0:35:53'}	<p><img alt="AMIGAAAAA" src="http://i.imgur.com/vlBaR.jpg" /></p>
87	estoy-flasheando-pedos-de-colo-20112032n	Estoy flasheando pedos de colores con un tema que escuché en el disco 	Estoy flasheando pedos de colores con un tema que escuché en el disco Litoral de Liliana Herrero.\r\nSe los dejo acá para que lo escuchen http://dl.dropbox.com/u/163405/Litoral/Track03.mp3 Y derramo un par de ideas:\r\n\r\nBuscando encontré que la canción es de una piba que se llama Ada Prada. No hay mucha data de la mina, hasta donde me da la paciencia para buscar.\r\n\r\nEncontré la letra acá con acordes http://lacuerda.net/tabs/a/ana_prada/tierra_adentro.shtml y un videito de youtube que tiene un audio decente http://www.youtube.com/watch?v=lCO_kB4LqpY\r\n\r\nLa versión que está en Litoral tiene arreglos muy parecidos a los originales, sin embargo, donde una es prolija y... bueno, "la original", la otra, que es una copia bastante ajustada, explota.\r\n\r\nEl original está como más áspero, Liliana es una cantante vieja y su voz fluye con una soltura que se consigue con los años, Ada como que canta más durita, con unos yeites en los fraseos que me parecen medio gastados. En eso, me parece que alguno menos "profesional" por ahí le saca más expresividad a la misma frase.\r\n\r\nLos invito a escuchar esta canción, hoy o mañana... repetidas veces si es posible.\r\n\r\n	tutuca	2010-10-14 22:52:53.001005-03	2011-01-21 23:32:31.157434-03	música, liliana herrero	{u'uptime': u'0 day, 7:40:2'}	<p>Estoy flasheando pedos de colores con un tema que escuché en el disco Litoral de Liliana Herrero.\nSe los dejo acá para que lo escuchen http://dl.dropbox.com/u/163405/Litoral/Track03.mp3 Y derramo un par de ideas:</p>\n<p>Buscando encontré que la canción es de una piba que se llama Ada Prada. No hay mucha data de la mina, hasta donde me da la paciencia para buscar.</p>\n<p>Encontré la letra acá con acordes http://lacuerda.net/tabs/a/ana_prada/tierra_adentro.shtml y un videito de youtube que tiene un audio decente http://www.youtube.com/watch?v=lCO_kB4LqpY</p>\n<p>La versión que está en Litoral tiene arreglos muy parecidos a los originales, sin embargo, donde una es prolija y... bueno, "la original", la otra, que es una copia bastante ajustada, explota.</p>\n<p>El original está como más áspero, Liliana es una cantante vieja y su voz fluye con una soltura que se consigue con los años, Ada como que canta más durita, con unos yeites en los fraseos que me parecen medio gastados. En eso, me parece que alguno menos "profesional" por ahí le saca más expresividad a la misma frase.</p>\n<p>Los invito a escuchar esta canción, hoy o mañana... repetidas veces si es posible.</p>
17	bureaucrat-conrad-you-are-tec-20112032n	Bureaucrat Conrad, you are technically correct -- the best kind of cor	Bureaucrat Conrad, you are technically correct -- the best kind of correct	anonymous	2010-08-24 15:50:03-03	2011-01-21 23:32:31.509856-03	r	{u'uptime': u'0 day, 6:8:22'}	<p>Bureaucrat Conrad, you are technically correct -- the best kind of correct</p>
30	reddit-me-hizo-ganar-una-cerve-20112032n	Reddit me hizo ganar una cerveza hoy\nSo what Python framework do you u	Reddit me hizo ganar una cerveza hoy\n\n    So what Python framework do you use?\n\n    [Pylons](http://pylonshq.com/). You can see our source code if you want. The data is stored in a PostgreSQL database and served by a combination of haproxy and nginx.\n\n\n	tutuca	2010-08-26 15:22:06-03	2011-01-21 23:32:31.707182-03	giladas	{u'uptime': u'0 day, 4:17:21'}	<p>Reddit me hizo ganar una cerveza hoy</p>\n<pre><code>So what Python framework do you use?\n\n[Pylons](http://pylonshq.com/). You can see our source code if you want. The data is stored in a PostgreSQL database and served by a combination of haproxy and nginx.\n</code></pre>
37	war-what-is-it-good-for-abso-20112032n	War. What is it good for? Absolutly nothing (War - Edwin Starr)	**[War. What is it good for? Absolutly nothing](http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/)** (War - Edwin Starr)\n\n	etnalubma	2010-08-27 14:33:03-03	2011-01-21 23:32:31.895139-03	video,edwin	{u'uptime': u'0 day, 4:29:47'}	<p><strong><a href="http://www.tylerlesmann.com/2009/apr/02/python-markdown-extension-video/">War. What is it good for? Absolutly nothing</a></strong> (War - Edwin Starr)</p>
2	from-djangocontribsyndicatio-20112032n	from django.contrib.syndication.views import Feed\nfrom ltmo.models imp	from django.contrib.syndication.views import Feed\r\nfrom ltmo.models import Leak\r\n\r\nclass LeakFeed(Feed):\r\n    title = "Derrames publicados recientemente"\r\n    link = "/"\r\n    description = "Derrames nuevos o actualizados"\r\n    description_template = 'feeds/description.html'\r\n\r\n    def items(self):\r\n        return Leak.objects.order_by("-created")[:15]\r\n\r\n    def item_title(self, item):\r\n        return item.title\r\n\r\n    def item_description(self, item):\r\n        return item.description	tutuca	2010-09-28 22:08:21-03	2011-01-21 23:32:31.933299-03	r	{u'uptime': u'0 day, 2:7:11'}	<p>from django.contrib.syndication.views import Feed\nfrom ltmo.models import Leak</p>\n<p>class LeakFeed(Feed):\n    title = "Derrames publicados recientemente"\n    link = "/"\n    description = "Derrames nuevos o actualizados"\n    description_template = 'feeds/description.html'</p>\n<pre><code>def items(self):\n    return Leak.objects.order_by("-created")[:15]\n\ndef item_title(self, item):\n    return item.title\n\ndef item_description(self, item):\n    return item.description\n</code></pre>
45	como-recuperar-el-aceite-perdi-20112032n	Como recuperar el aceite perdido\nAcabo de encontrar un artículo en Hac	Como recuperar el aceite perdido\n--------------------------------\nAcabo de encontrar un artículo en [Hack a Day](http://hackaday.com) sobre\ncomo recuperar el aceite derramado en el agua de manera no invasiva usando\nrobótica y una nanofabrica absorbente de aceite. Esperemos que este tipo\nde enfoques tecnológicos sean cada vez mas frecuentes.\n\n[Ver artículo](http://hackaday.com/2010/08/29/seaswarm-we-can-clean-up-the-gulf-in-a-month/)	etnalubma	2010-08-31 11:48:45-03	2011-01-21 23:32:32.001907-03	tecnologia,articulo	{u'uptime': u'0 day, 1:39:21'}	<h2>Como recuperar el aceite perdido</h2>\n<p>Acabo de encontrar un artículo en <a href="http://hackaday.com">Hack a Day</a> sobre\ncomo recuperar el aceite derramado en el agua de manera no invasiva usando\nrobótica y una nanofabrica absorbente de aceite. Esperemos que este tipo\nde enfoques tecnológicos sean cada vez mas frecuentes.</p>\n<p><a href="http://hackaday.com/2010/08/29/seaswarm-we-can-clean-up-the-gulf-in-a-month/">Ver artículo</a></p>
\.


--
-- Data for Name: south_migrationhistory; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY south_migrationhistory (id, app_name, migration, applied) FROM stdin;
1	ltmo	0001_initial	2010-11-10 02:14:27.346833-03
2	ltmo	0002_auto__add_field_leak_rendered	2010-11-10 02:15:08.993195-03
\.


--
-- Data for Name: tagging_tag; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY tagging_tag (id, name) FROM stdin;
1	frases
2	inenieria
3	ingenieria
4	giladas
5	raro
6	r
7	reflexiones
8	seo
9	gif
10	frase
11	test
12	buildout
13	django
14	python
15	solr
16	supervisord
17	varnish
18	gorilas
19	videito
20	sagan
21	video
22	pruebas
23	prueba
24	oesterheld
25	codigo
26	spill
27	trucos
28	edwin
29	bash
30	animacion
31	blender
32	articulo
33	tecnologia
34	chachacha
35	comida
36	debian
37	linux
38	peron
39	san martin
40	foto
41	tiempo
42	fractales
43	windows
44	fluidos
45	humor
46	javier fresser
47	mierda
48	2001
49	kurbic
50	charlas
51	unrelated
52	historieta
53	liniers
54	decara
55	fail
56	chavo
57	imagen
58	ffffffffuuuuuuuu
59	cafe
60	panda
61	flash
62	sueños
63	vader
64	sorry
65	videos
66	liliana herrero
67	música
68	read
69	videla
\.


--
-- Data for Name: tagging_taggeditem; Type: TABLE DATA; Schema: public; Owner: ltmo
--

COPY tagging_taggeditem (id, tag_id, content_type_id, object_id) FROM stdin;
7	6	10	1
8	6	10	2
10	8	10	4
11	6	10	5
12	9	10	6
13	9	10	7
14	10	10	8
15	10	10	9
16	11	10	10
17	11	10	11
18	1	10	12
19	12	10	13
20	13	10	13
21	14	10	13
22	15	10	13
23	16	10	13
24	17	10	13
25	9	10	14
26	9	10	15
27	18	10	16
28	6	10	17
29	19	10	18
30	20	10	19
31	21	10	19
32	10	10	20
33	20	10	20
34	6	10	21
35	6	10	22
36	6	10	23
37	6	10	24
38	22	10	25
39	22	10	26
40	23	10	27
41	6	10	28
42	4	10	29
43	4	10	30
44	11	10	31
45	11	10	32
46	24	10	33
47	24	10	34
48	25	10	35
49	26	10	35
50	27	10	35
51	25	10	36
52	26	10	36
53	27	10	36
54	28	10	37
55	21	10	37
56	28	10	38
57	21	10	38
58	6	10	39
59	29	10	40
60	30	10	41
61	31	10	41
62	9	10	41
63	31	10	42
64	30	10	43
65	9	10	43
66	6	10	44
67	32	10	45
68	33	10	45
69	34	10	46
70	21	10	46
71	35	10	47
72	6	10	48
73	29	10	49
74	27	10	49
75	21	10	50
76	6	10	51
77	1	10	52
78	36	10	53
79	37	10	53
80	38	10	53
81	39	10	53
82	40	10	54
83	41	10	54
84	42	10	55
85	21	10	55
86	32	10	56
87	37	10	56
88	43	10	56
89	30	10	57
90	31	10	57
91	44	10	57
92	6	10	58
93	45	10	59
94	9	10	60
95	45	10	60
96	9	10	61
97	46	10	62
98	21	10	62
99	47	10	63
100	48	10	64
101	49	10	64
102	21	10	64
103	50	10	65
104	1	10	66
105	40	10	67
106	51	10	67
107	52	10	68
108	53	10	68
109	6	10	69
110	6	10	70
111	54	10	71
112	55	10	72
113	40	10	72
114	56	10	73
115	57	10	73
116	58	10	74
117	14	10	75
118	59	10	76
119	9	10	76
120	60	10	76
121	9	10	77
122	9	10	78
123	30	10	79
124	61	10	79
125	62	10	79
126	40	10	80
127	63	10	80
129	64	10	81
130	65	10	82
131	6	10	83
132	6	10	84
133	6	10	85
134	6	10	86
136	66	10	87
137	67	10	87
138	68	10	88
139	9	10	89
140	6	10	90
141	9	10	91
142	69	10	92
143	6	10	3
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_message_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT auth_message_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: ltmo_leak_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY ltmo_leak
    ADD CONSTRAINT ltmo_leak_pkey PRIMARY KEY (id);


--
-- Name: south_migrationhistory_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY south_migrationhistory
    ADD CONSTRAINT south_migrationhistory_pkey PRIMARY KEY (id);


--
-- Name: tagging_tag_name_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY tagging_tag
    ADD CONSTRAINT tagging_tag_name_key UNIQUE (name);


--
-- Name: tagging_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY tagging_tag
    ADD CONSTRAINT tagging_tag_pkey PRIMARY KEY (id);


--
-- Name: tagging_taggeditem_pkey; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY tagging_taggeditem
    ADD CONSTRAINT tagging_taggeditem_pkey PRIMARY KEY (id);


--
-- Name: tagging_taggeditem_tag_id_key; Type: CONSTRAINT; Schema: public; Owner: ltmo; Tablespace: 
--

ALTER TABLE ONLY tagging_taggeditem
    ADD CONSTRAINT tagging_taggeditem_tag_id_key UNIQUE (tag_id, content_type_id, object_id);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_message_user_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_message_user_id ON auth_message USING btree (user_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: tagging_taggeditem_content_type_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX tagging_taggeditem_content_type_id ON tagging_taggeditem USING btree (content_type_id);


--
-- Name: tagging_taggeditem_object_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX tagging_taggeditem_object_id ON tagging_taggeditem USING btree (object_id);


--
-- Name: tagging_taggeditem_tag_id; Type: INDEX; Schema: public; Owner: ltmo; Tablespace: 
--

CREATE INDEX tagging_taggeditem_tag_id ON tagging_taggeditem USING btree (tag_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_message_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT auth_message_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_3cea63fe; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tagging_taggeditem_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY tagging_taggeditem
    ADD CONSTRAINT tagging_taggeditem_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: tagging_taggeditem_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY tagging_taggeditem
    ADD CONSTRAINT tagging_taggeditem_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES tagging_tag(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_7ceef80f; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_7ceef80f FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_dfbab7d; Type: FK CONSTRAINT; Schema: public; Owner: ltmo
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_dfbab7d FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--


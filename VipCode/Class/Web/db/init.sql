-- 重新设置字符格式命令
set character_set_client=utf8;
set character_set_connection=utf8;
set character_set_database=utf8mb4;
set character_set_results=gb2312;
set character_set_server=utf8;

-- 使用数据库 bk
use bk;

-- 创建城市表
create table city (
  `id` smallint(4) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL DEFAULT '' COMMENT '城市名称',
  `city_code` mediumint(6) UNSIGNED NOT NULL DEFAULT 0 COMMENT '城市代码',
  `province_code` mediumint(6) UNSIGNED NOT NULL DEFAULT 0 COMMENT '省份代码',
  `description`  TEXT COMMENT '介绍',
  PRIMARY KEY (`id`),
  KEY `province_code` (`province_code`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='城市表';

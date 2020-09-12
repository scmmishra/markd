const path = require('path');
const fs = require('fs');
const sites_path = path.resolve('../../../sites');
const common_site_config = require('../../../sites/common_site_config.json');
const { webserver_port } = common_site_config;
const sites = fs
	.readdirSync(sites_path)
	.filter(
		folder_name =>
			![
				'.build',
				'apps.txt',
				'assets',
				'common_site_config',
				'currentsite'
			].includes(folder_name)
	);

// FRAPPE_ENV will be either undefined, 'development' or 'production'
if (process.env.FRAPPE_ENV) {
	process.env.NODE_ENV = process.env.FRAPPE_ENV;
}

const serverProxy = {
	target: `http://localhost:${webserver_port}`,
	ws: true,
	changeOrigin: true,
	router: function (req) {
		const site_name = req.headers.host.split(':')[0];
		return `http://${site_name}:${webserver_port}`;
	}
}

module.exports = {
	publicPath:
		process.env.NODE_ENV === 'production' ? '/assets/markd/dashboard/' : '/',
	outputDir: path.resolve('../markd/public/dashboard'),
	indexPath: path.resolve('../markd/www/dashboard.html'),
	devServer: {
		allowedHosts: sites,
		proxy: {
			'^/api': serverProxy,
			'^/assets': serverProxy,
			'^/files': serverProxy
		}
	}
};

export default async function call(method, args) {
	if (!args) {
		args = {};
	}

	const headers = {
		Accept: 'application/json',
		'Content-Type': 'application/json; charset=utf-8',
		'X-Frappe-Site-Name': window.location.hostname
	}

	if (window.csrf_token && window.csrf_token !== '{{ csrf_token }}') {
		headers['X-Frappe-CSRF-Token'] = window.csrf_token;
	}

	const res = await fetch(`/api/method/markd.markd.api.${method}`, {
		method: 'POST',
		headers,
		body: JSON.stringify(args)
	});

	if (res.ok) {
		const data = await res.json();
		console.log(data)
		if (data.docs) {
			return data;
		}
		return data.message;
	} else {
		let error = null;
		let data = null;
		try {
			data = await res.json();
			if (data.exc) {
				error = JSON.parse(data.exc)[0];
			}
		} catch (e) {
			error = await res.text();
		}
		console.error(error);
		return {
			error: true,
			data
		};
	}
}
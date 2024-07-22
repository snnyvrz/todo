async function getData() {
  const res = await fetch("http://localhost:8000");
  if (!res.ok) {
    throw new Error("Failed to fetch data");
  }

  return res.json();
}

export default async function Page() {
  const data = await getData();

  return <main>{data["Hello"]}</main>;
}

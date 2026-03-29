New-Item -ItemType Directory -Force -Path chapters\images

$html = Get-Content doc.html -Raw
$matches = [regex]::Matches($html, '<img[^>]+src="(data:image/([^;]+);base64,([^"]+))"')
for ($i=0; $i -lt $matches.Count; $i++) {
    $ext = $matches[$i].Groups[2].Value
    if ($ext -eq "jpeg") { $ext = "jpg" }
    
    $b64 = $matches[$i].Groups[3].Value
    $bytes = [Convert]::FromBase64String($b64)
    $path = "chapters\images\img_${i}.${ext}"
    [System.IO.File]::WriteAllBytes((Resolve-Path .\chapters\images).Path + "\img_${i}.${ext}", $bytes)
    Write-Host "Extracted img_${i}.${ext}"
}

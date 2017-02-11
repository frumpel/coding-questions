$string="asdf";

@string=split /\s*/,$string;

foreach $a (@string) {
	$a{$a}++;
}

foreach $a (sort keys(%a)) {
	# print "$a: $a{$a}\n";
	if ($a{$a}>1) {
		print "Duplicates present\n";
		 exit;
	}
}
print "No Duplicates\n";
exit;

